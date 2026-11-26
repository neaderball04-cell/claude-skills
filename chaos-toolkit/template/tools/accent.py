import re
W={'the':'ze','this':'zis','that':'zat','these':'zese','those':'zose','they':'zey','them':'zem','their':'zeir','there':'zere','then':'zen','than':'zan',
'think':'sink','thing':'sing','things':'sings','three':'sree','through':'srough','thirty':'sirty','with':'vis','without':'visout','what':'vat','when':'ven',
'where':'vere','why':'vy','who':'who','whole':'whole','yes':'ja','first':'first','everything':'everysing','nothing':'nossing','something':'somesing','trust':'trust'}
def fix(w):
    lw=w.lower()
    if lw in W: r=W[lw]
    elif re.match(r'w[aeiyo]',lw) and lw not in ('who','whom','whose','women','woman','would','world','words','word','wolf'): r='v'+lw[1:]
    elif lw.startswith('th'): r='z'+lw[2:]
    else: return w
    return r[0].upper()+r[1:] if w[0].isupper() else r
def german(t):
    t=t.replace('Hey hey,','Guten Tag,').replace('Ohhh boy.','Ach du lieber.').replace('Uh oh.','Achtung! Uh oh.')
    t=re.sub(r'^(Step \w+!)',r'Achtung! \1',t)
    t=re.sub(r"[A-Za-z][A-Za-z']*",lambda m:fix(m.group(0)),t)
    return t
if __name__=='__main__':
    print(german("Step one! Read the 5434 like an intel report. Detective mode! Then call them, with your backup. What worries them? We will wait."))
