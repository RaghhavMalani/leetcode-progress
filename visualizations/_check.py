import io,os,re,subprocess,sys,glob,json
ROOT=os.path.dirname(os.path.abspath(__file__))
STUB = """
var document={title:'',currentScript:{getAttribute:function(){return '_engine.js';}},
  getElementsByTagName:function(){return [{getAttribute:function(){return '_engine.js';}}];},body:{appendChild:function(){}},createElement:function(){return {};},
  getElementById:function(){return {style:{},classList:{add:function(){},remove:function(){}},
    querySelectorAll:function(){return [];},querySelector:function(){return null;},
    scrollIntoView:function(){}};},
  querySelectorAll:function(){return [];},addEventListener:function(){}};
var window=globalThis;
"""
def check(files):
    eng = io.open(os.path.join(ROOT,'_engine.js'),encoding='utf-8').read()
    bad=[]
    for f in files:
        html = io.open(f,encoding='utf-8').read()
        m = re.findall(r'<script>([\s\S]*?)</script>', html)
        body = '\n'.join(m)
        # capture what LV.render receives instead of rendering
        harness = STUB + eng + """
var __spec=null; LV.render=function(s){__spec=s;};
""" + body + """
if(!__spec) throw new Error('LV.render never called');
var T=__spec.build();
if(!T.events.length) throw new Error('no events');
T.events.forEach(function(e,i){
  if(typeof e.line!=='number'||e.line<1||e.line>__spec.src.length)
    throw new Error('event '+i+' bad line '+e.line+' (src has '+__spec.src.length+' lines)');
  if(!e.msg) throw new Error('event '+i+' empty msg');
});
console.log(JSON.stringify({slug:__spec.slug,steps:T.events.length,out:T.out}));
"""
        p = subprocess.run(['node','-e',harness],capture_output=True,text=True)
        if p.returncode:
            bad.append((os.path.basename(f), p.stderr.strip().split('\n')[-3:]))
        else:
            print('  ok  '+p.stdout.strip())
    for b in bad:
        print('  FAIL '+b[0]); [print('       '+x) for x in b[1]]
    return len(bad)

if __name__=='__main__':
    fs = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT,'0*.html')))
    n = check(fs)
    print(('%d failures'%n) if n else 'all clean')
    sys.exit(1 if n else 0)
