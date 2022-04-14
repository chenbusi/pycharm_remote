properties([parameters([string(defaultValue: 'chen', description: 'what;s your name?', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * *')])])

node {
    stage("clone") {
        git "https://github.com/chenbusi/pycharm_remote.git"
    }
    stage("bla") {
        sh "ls -l"
    }
 }
