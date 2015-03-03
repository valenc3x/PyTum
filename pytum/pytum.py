__author__ = 'avathar'

import os
from stat import S_IXUSR

COMMANDS = {
    '.takeoff': 'rostopic pub -1 /ardrone/takeoff std_msgs/Empty',
    '.land': 'rostopic pub -1 /ardrone/land std_msgs/Empty',
    '.zero': '',
    # commands with args
    '.forward': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.backward': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: -1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.left': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 1.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.right': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: -1.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.up': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 1.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.down': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: -1.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.cw': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: -1.0}}'",
    '.ccw': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 1.0}}'",
    '.hover': "",
    '.wait': "",
    '.go': "",

}


class Pytum:
    def __init__(self, filename):
        self.file = filename
        self.instructions = []

    def parse_file(self):
        print "parse_file"
        input = open(self.file)
        content = input.readlines()
        for line in content:
            # remove comments
            line = line.split('//')[0]
            # remove line breaks and leading spaces
            line = line.replace('\n', '').strip()
            for command in COMMANDS.keys():
                if command in line:
                    print COMMANDS[command]
                    self.instructions.append(COMMANDS[command])
        input.close()

    def make_script(self):
        name = self.file.partition('.')[0]
        filename = name + '.pt'
        output = open(filename, 'w')
        for command in self.instructions:
            output.write(command)
            output.write('\n')
        # try:
        #     os.chmod(filename, S_IXUSR)
        # except IOError:
        #     print "Error making runnable file"
        output.close()
