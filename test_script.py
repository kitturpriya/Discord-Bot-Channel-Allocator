import discord
from discord.ext import commands
from Gdrivetest import auth
import utils
import time
import random

# responses=auth()
# print(responses)
# mem_com = entries_from_sheet()
mem_com = {'priyanka kittur': ['company-a'], 'tanay yadav': ['Company-A', 'company-b']}
companies_intr = ['company-a', 'company-b', 'company-c']

intents = discord.Intents.all()
intents.guilds=True
intents.members=True
intents.presences=True
bot = discord.Client(intents = intents)


members = []
interviewees = []


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == "pri's server":
            for member in guild.members:

                if member.nick is not None:
                    members.append(member.nick)

    for name in members:
        if name[:2] == 'p_':
            interviewees.append(name[2:].lower())
    
    print('Bot Ready!')


@bot.event
async def on_message(message):

    if message.content == '--die':       
        await bot.close()
        print('Bot Closed')
    
    if message.content == 'alloc':        
        for guild in bot.guilds:            
            if guild.name == "pri's server":

                ########### INITIAL ALLOCATION PROCESS ###########
                
                for i in mem_com.keys():

                    m_d = utils.mem_dict(guild.members)
                    vc_d = utils.vc_dict(guild.voice_channels)
                    
                    if i in interviewees and m_d[i] in bot.get_channel(994312971092234290).members: 
                        
                        wd = utils.wait_dict(guild.voice_channels)
                        companies = mem_com[i]
                        least = 10000
                        
                        for company, no in wd.items():                            
                            if company in companies and no<least:
                                
                                least=no
                                x=company
                        
                        channel_aloc = vc_d[x+"_wait"]                     
                        await m_d[i].move_to(channel_aloc)
                        print(f'{m_d[i].nick} moved.', wd)
                
                # time.sleep (1)                                                 # we wait for 5 minutes
                
                ########## INTERVIEW ALLOCATION PROCESS ##########
                name_id_d = utils.name_id(guild.voice_channels)
                while (True):
                    time.sleep(2)
                    wait_list = utils.wait_dict(guild.voice_channels)
                    if max(list(wait_list.values())) > 0:
                        for company in companies_intr:                          
                            i_d = utils.intr_dict(utils.vc_dict(guild.voice_channels))
                            
                            print(f'wl: {wait_list[company.lower()]}, members in {company}: {len(bot.get_channel(name_id_d[company]).voice_states)}')
                            
                            if len(bot.get_channel(name_id_d[company.lower()]).members) == 0 and wait_list[company.lower()] > 0:
                                
                                print('Here', company)
                                text_channel = discord.utils.get(guild.text_channels, name=company + '_w') 
                                temp_mems = list(vc_d[company + '_wait'].members)
                                print(temp_mems)
                                random.shuffle(temp_mems)
                                member = temp_mems[0]
                                channel_to = vc_d[company + '_intr']
                                await text_channel.send(f'{member.mention} You are up next for the interview! Type "admit" in the next 60 seconds.')
                                time.sleep(15)
                                text_history = await text_channel.history(limit=1).flatten()
                                print(text_history[0].content)
                                if text_history[0].content == 'admit':
                                    print(f'Moving {member.nick} to {channel_to.name}')
                                    await member.move_to(channel_to)
                                # else:

                    else:
                        print('No more interviewees in the waiting lists!')
                        break
                    # sd = utils.state_dict ()
@ bot.event
async def on_voice_state_update(member, before, after):
    print(f'{member.nick} moved from {before.channel.name} to {after.channel.name}')

bot.run()