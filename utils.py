def mem_dict(members):
    m_dict = {}
    for i in range(len(members)):
        if members[i].nick is not None and members[i].nick[:2] == 'p_':
            name = members[i].nick.lower()[2:]
            m_dict[name] = members[i]

    return m_dict


def vc_dict(channels):
    v_dict = {}
    for channel in channels:
        if channel.position <10:
            if channel.name[-2:] == '_w':
                name = channel.name + 'ait'
                v_dict[name] = channel

            else:
                name = channel.name + '_intr'
                v_dict[name] = channel

    return v_dict


def wait_dict(channels):
    wd = {}
    for channel in channels:
        if channel.name[-2:] == '_w':
            l = len(channel.name)
            wd[channel.name[0:l-2]] = len(channel.members)

    return wd

def num_mem(channel):
    count = 0
    for member in channel.members:
        if member.name[:2] == 'p_':
            count = 1

    if count == 0:
        return True
    else:
        return 
        

def intr_dict(vcd):
    channels = []
    for name, channel in vcd.items():
        if name[-5:] == '_intr':
            channels.append(channel)

    wd = {}
    for channel in channels:
        wd[channel.name] = len(channel.members)

    return wd


def name_id (voice_channels):
    n_id = {}
    for channel in voice_channels:
        n_id[channel.name] = channel.id

    return n_id