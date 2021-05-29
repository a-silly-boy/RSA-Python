import resources
import commands


while True:
    args = input(resources.name + resources.pos + resources.prompt).split(' ')
    commands.execute(args[0], *args[1:])
