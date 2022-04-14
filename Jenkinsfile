properties([pipelineTriggers([pollSCM('* * * * *')])])

node {
    stage("clone") {
        git "https://github.com/chenbusi/pycharm_remote.git"
    }
    stage("bla") {
        sh "ls -l"
    }
 }
