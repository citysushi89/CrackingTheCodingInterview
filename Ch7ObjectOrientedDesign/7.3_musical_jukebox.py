"""
Design a musical jukebox using OO principles
"""

"""
Things to include in an init:
buttons (play, stop, FF, RW)
elements: CD Holder, plug
"""
# def __init__(self, type, play_button, stop_button, fast_forward_button, rewind_button, plug='unplugged', cd_holder='closed'):

class JukeBox:
    def __init__(self, type, status='off', plug='unplugged', cd_holder='empty', is_ready=False, playing=False, cd_name=''):
        self.type = type
        self.plug = plug
        self.cd_holder = cd_holder
        self.status = status
        self.is_ready = is_ready
        self.playing = playing

    def setup(self):
        self.plug = 'plugged in'
        self.status = 'on'
        self.cd_holder = 'filled'
        self.is_ready = True

    def play(self):
        if not self.is_ready:
            return 'ERROR: jukebox not setup'
        self.playing = True
        return 'Music Playing'

    def stop(self):
        if not self.playing:
            return "ERROR: nothing playing"
        self.playing = False
        return 'Music Stopped'

    def put_in_cd(self, name_of_cd):
        if self.playing:
            return "ERROR: opened during music playing"
        print('opened')
        print(f'cd {name_of_cd} put in')
        return 'closed'


# User can uncomment a below line to 
jb = JukeBox(type='cd')
jb.setup()
print(jb.play())
print(jb.stop())
print(jb.put_in_cd('Chief'))
print(jb.play())