__author__ = 'avathar'

import os
import stat

COMMAND_STOP = "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}' & sleep 1 & killall rostopic $! \n"

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
    '.altitude': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 1.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.down': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: -1.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'",
    '.cw': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: -1.0}}'",
    '.ccw': "rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 1.0}}'",
    # '.hover': "",
    # '.wait': "",
    '.go': "",
}

instructions = []

def command_with_args(command, value):
    print command, value
    new_command = '' 
    new_command += COMMANDS[command] + ' & \n'
    new_command += 'sleep ' + str(value) + ' \n'
    new_command += 'killall rostopic \n'
    new_command += COMMAND_STOP
    return new_command

def make_script(filename):
    name = filename.partition('.')[0]
    output_file = name + '.pt'
    print output_file
    output = open(output_file, 'w')
    for command in instructions:
        output.write(command)
        output.write('\n')
    # try:
    #     os.chmod(output_file, stat.S_IXUSR)
    # except IOError:
    #     print "Error making runnable file"
    output.close()


#  Main function
def parse_file(filename=''):
    print "parsing file..."
    input_file = open(filename)
    content = input_file.readlines()
    for line in content:
        # remove comments
        line = line.split('//')[0]
        # remove line breaks and leading spaces
        line = line.replace('\n', '').strip()
        for command in COMMANDS.keys():
            if command in line:
                read_args = line.replace('(','#').replace(')','')
                func_args = read_args.partition('#')
                if  func_args[2].isdigit():
                    value =  int(func_args[2])
                    new_command = command_with_args(func_args[0], value)
                    instructions.append(new_command)
                else:
                    instructions.append(COMMANDS[command])
    input_file.close()

    make_script(filename)

