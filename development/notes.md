- https://www.tutorialspoint.com/online_ruby_formatter.htm

## installed tools
check manually to remove overhead

Start-Date: 2019-01-25  21:05:24
Commandline: apt install -y ruby
Requested-By: vagrant (1000)
Install: javascript-common:amd64 (11, automatic), ruby2.5:amd64 (2.5.1-1ubuntu1.1, automatic), rake:amd64 (12.3.1-1, automatic), ruby-net-telnet:amd64 (0.1.1-2, automatic), libjs-jquery:amd64 (3.2.1-1, automatic), ruby-minitest:amd64 (5.10.3-1, automatic), libruby2.5:amd64 (2.5.1-1ubuntu1.1, automatic), ruby:amd64 (1:2.5.1), ruby-power-assert:amd64 (0.3.0-1, automatic), unzip:amd64 (6.0-21ubuntu1, automatic), zip:amd64 (3.0-11build1, automatic), rubygems-integration:amd64 (1.11, automatic), fonts-lato:amd64 (2.0-2, automatic), ruby-test-unit:amd64 (3.2.5-1, automatic), ruby-did-you-mean:amd64 (1.2.0-2, automatic)
End-Date: 2019-01-25  21:05:30

Start-Date: 2019-01-25  21:06:46
Commandline: apt install -y python3-pip
Requested-By: vagrant (1000)
Install: libmpc3:amd64 (1.1.0-1, automatic), libgcc-7-dev:amd64 (7.3.0-27ubuntu1~18.04, automatic), libmpx2:amd64 (8.2.0-1ubuntu2~18.04, automatic), python3-dev:amd64 (3.6.7-1~18.04, automatic), python3-distutils:amd64 (3.6.7-1~18.04, automatic), linux-libc-dev:amd64 (4.15.0-43.46, automatic), libfakeroot:amd64 (1.22-2ubuntu1, automatic), libc6-dev:amd64 (2.27-3ubuntu1, automatic), libpython3.6-dev:amd64 (3.6.7-1~18.04, automatic), libexpat1-dev:amd64 (2.2.5-3, automatic), cpp-7:amd64 (7.3.0-27ubuntu1~18.04, automatic), libalgorithm-diff-perl:amd64 (1.19.03-1, automatic), libalgorithm-merge-perl:amd64 (0.08-3, automatic), binutils:amd64 (2.30-21ubuntu1~18.04, automatic), cpp:amd64 (4:7.3.0-3ubuntu2.1, automatic), libitm1:amd64 (8.2.0-1ubuntu2~18.04, automatic), g++:amd64 (4:7.3.0-3ubuntu2.1, automatic), python3-pip:amd64 (9.0.1-2.3~ubuntu1), python3-keyring:amd64 (10.6.0-1, automatic), python3-wheel:amd64 (0.30.0-0.2, automatic), gcc-7-base:amd64 (7.3.0-27ubuntu1~18.04, automatic), gcc:amd64 (4:7.3.0-3ubuntu2.1, automatic), libcilkrts5:amd64 (7.3.0-27ubuntu1~18.04, automatic), libasan4:amd64 (7.3.0-27ubuntu1~18.04, automatic), libquadmath0:amd64 (8.2.0-1ubuntu2~18.04, automatic), libisl19:amd64 (0.19-1, automatic), build-essential:amd64 (12.4ubuntu1, automatic), libfile-fcntllock-perl:amd64 (0.22-3build2, automatic), python3-xdg:amd64 (0.25-4ubuntu1, automatic), binutils-x86-64-linux-gnu:amd64 (2.30-21ubuntu1~18.04, automatic), libstdc++-7-dev:amd64 (7.3.0-27ubuntu1~18.04, automatic), libtsan0:amd64 (8.2.0-1ubuntu2~18.04, automatic), libubsan0:amd64 (7.3.0-27ubuntu1~18.04, automatic), g++-7:amd64 (7.3.0-27ubuntu1~18.04, automatic), make:amd64 (4.1-9.1ubuntu1, automatic), fakeroot:amd64 (1.22-2ubuntu1, automatic), gcc-7:amd64 (7.3.0-27ubuntu1~18.04, automatic), python3-lib2to3:amd64 (3.6.7-1~18.04, automatic), liblsan0:amd64 (8.2.0-1ubuntu2~18.04, automatic), libgomp1:amd64 (8.2.0-1ubuntu2~18.04, automatic), dh-python:amd64 (3.20180325ubuntu2, automatic), manpages-dev:amd64 (4.15-1, automatic), binutils-common:amd64 (2.30-21ubuntu1~18.04, automatic), python3-keyrings.alt:amd64 (3.0-1, automatic), libc-dev-bin:amd64 (2.27-3ubuntu1, automatic), python3-crypto:amd64 (2.6.1-8ubuntu2, automatic), libbinutils:amd64 (2.30-21ubuntu1~18.04, automatic), libpython3-dev:amd64 (3.6.7-1~18.04, automatic), libatomic1:amd64 (8.2.0-1ubuntu2~18.04, automatic), libcc1-0:amd64 (8.2.0-1ubuntu2~18.04, automatic), python3.6-dev:amd64 (3.6.7-1~18.04, automatic), libdpkg-perl:amd64 (1.19.0.5ubuntu2.1, automatic), python3-secretstorage:amd64 (2.3.1-2, automatic), libalgorithm-diff-xs-perl:amd64 (0.04-5, automatic), python-pip-whl:amd64 (9.0.1-2.3~ubuntu1, automatic), python3-setuptools:amd64 (39.0.1-2, automatic), dpkg-dev:amd64 (1.19.0.5ubuntu2.1, automatic)
End-Date: 2019-01-25  21:07:42

## todo - features
- start stop traning
    - admindojo training start
        - read tuptime and save to /vagrant/tmp/training_start (seconds). calc training time tuptime-total - training-start
    - admindojo training status
        - run inspec without result
    - admindojo training finish
        - run inspec with result
        - save tuptime to /vagrant/tmp/training_end
        - save result to /admindojo/result/trainingname
        - copy training_start + training_end to /admindojo/result/trainingname  
