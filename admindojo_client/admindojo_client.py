#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import logging
import logging.handlers
from configparser import ConfigParser
import json
from termcolor import colored
from subprocess import check_output
import subprocess
import shlex


logger = logging.getLogger('gamifier')


class ResultTraining(object):
    PlayerImpact = 0.0
    TrainingTimeLimit = 0
    TrainingTotalImpact = 0.0
    PlayerProductivity = 0
    PlayerTimeNeeded = 0.0

    def getUptime(self):
        tuptime = subprocess.check_output('tuptime -s | grep life | cut -d: -f2', shell=True)
        uptime = float(tuptime.decode('utf-8').strip())
        uptime = uptime/60
        uptime = round(uptime)
        return int(uptime)

    def setTimeLimit(self, time):
        self.TrainingTimeLimit = time
        self.PlayerTimeNeeded = self.getUptime()
        self.PlayerProductivity = round((time / self.PlayerTimeNeeded) * 100)

    def getResult(self):
        if (self.TrainingTotalImpact == self.PlayerImpact) and self.PlayerProductivity >= 90:
            return True
        else:
            return False


def main():
    resultTraining = ResultTraining()

    # Read JSON data into the datastore variable
    with open('json.json', 'r') as f:
        datastore = json.load(f)
        # todo try catch



    # calc total time
    # calc total impact
    for key in datastore['profiles']:
        timeneeded = 0
        for control in key['controls']:
            timeneeded += int(control['tags']['duration'])
            resultTraining.TrainingTotalImpact += control['impact']
    resultTraining.setTimeLimit(timeneeded)

    print()
    print("Result for Training: " + datastore['profiles'][0]['title'])
    print("Training id        : " + datastore['profiles'][0]['name'])
    # todo print help url

    print('---------------------------------------------------------')

    for key in datastore['profiles']:
        for control in key['controls']:
            print(control['title'])
            controlHasFailures = False
            for code in control['results']:
                if code['status'] == 'passed':
                    pass_color = 'green'
                    pass_symbol = "\N{check mark}"
                else:
                    pass_color = 'red'
                    pass_symbol = "\N{BALLOT X}"
                    controlHasFailures = True
                print('\t' + colored(pass_symbol, pass_color) + " " + code['code_desc'])

            print()
            print('\tEstimated duration: ' + str(control['tags']['duration']) + ' Minutes')
            print('\tPossible Impact   : ' + str(control['impact']))

            if controlHasFailures == True:
                # print tag help
                print('\t' + colored("This part has failures!", 'red'))
                print('\t\t' + 'See help: url')
            else:
                resultTraining.PlayerImpact += control['impact']

    print('---------------------------------------------------------')
    print()
    print('Total impact to earn: ' + str(resultTraining.TrainingTotalImpact))
    print('You got             : ' + str(resultTraining.PlayerImpact))
    print()
    print('Your time limit was : ' + str(resultTraining.TrainingTimeLimit) + ' Minutes')
    print('You needed          : ' + str(resultTraining.PlayerTimeNeeded) + ' Minutes')

    print('Productivity        : ' + str(resultTraining.PlayerProductivity) + '%')

    print()

    if resultTraining.getResult():
        print(colored("You finished your Task successfully!", 'green'))
    else:
        print(colored("You failed your Task. You need to pass all test and need a productivity of minimum 90%!", 'red'))
    print()

if __name__ == '__main__':
    main()
