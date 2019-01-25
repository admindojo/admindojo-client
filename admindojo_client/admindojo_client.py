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

logger = logging.getLogger('gamifier')


class ResultTraining(object):
    PlayerTimeNeeded = 0
    PlayerImpact = 0.0

    TrainingTimeLimit = 0
    TrainingTotalImpact = 0.0

    # total percentage
    # total score



def main():
    resultTraining = ResultTraining()

    # Read JSON data into the datastore variable
    with open('json.json', 'r') as f:
        datastore = json.load(f)
        # todo try catch



    # calc total time
    # calc total impact
    for key in datastore['profiles']:
        for control in key['controls']:
            ResultTraining.TrainingTimeLimit += int(control['tags']['duration'])
            ResultTraining.TrainingTotalImpact += control['impact']

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
                ResultTraining.PlayerImpact += control['impact']

    print('---------------------------------------------------------')
    print()
    print('Total impact to earn: ' + str(ResultTraining.TrainingTotalImpact))
    print('You got             : ' + str(ResultTraining.PlayerImpact))
    print()
    print('Your time limit was: ' + str(ResultTraining.TrainingTimeLimit) + ' Minutes')
    print('You needed         :')

    ResultTraining.PlayerTimeNeeded = 15

    tpm = ResultTraining.TrainingTimeLimit / ResultTraining.PlayerTimeNeeded
    print('TPM: ' + str(tpm))

    pentalty = float(ResultTraining.TrainingTotalImpact) * 0.7

    print('\t\t' + ' - Time Penalty: ' + str(pentalty))
    result = ResultTraining.PlayerImpact - pentalty
    print('Your result: ' + str(result))
    print()

    print("db")

    #output = subprocess.check_output(["echo", "Hello World!"])

    print('ende')

if __name__ == '__main__':
    main()
