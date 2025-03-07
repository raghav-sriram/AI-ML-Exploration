import math
import random
import string
import sys
POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = 0.75
CROSSOVER_LOCATIONS = 10
MUTATION_RATE = 0.8

ngrams_dict = {line.split()[0]: int(line.split()[1]) for line in open("ngrams.txt")}


def switch_out(zero, one, two):
    return zero[:one]+zero[two]+zero[one + 1:two]+ zero[one]+zero[two + 1:]

def gno_switch_out(s): #igno_switch_iout
    i, j = random.randint(0, len(s) - 1), random.randint(0, len(s) - 1); return s if i == j else switch_out(s, min(i, j), max(i, j))


def fitness(n, decipher, replace):
    record = 0
    stlsing = replace
    sly = dict()
    for i, char in enumerate(stlsing):
        uppercase_char = char.upper()
        uppercase_pseudo_cipher = string.ascii_uppercase[i].upper()
        sly[uppercase_char] = uppercase_pseudo_cipher
    syph = sly
    words = "".join([syph[char.upper()] if char.upper() in syph else char for char in decipher])

    for i in range(0,1+len(words) - n):
        ngram = words[i:i + n]

        if ngram in ngrams_dict and ngram.isalpha(): record = record + math.log(ngrams_dict[ngram], 2)

    return record



def hill_climbing(n, decipher):
    how_fit = fitness(n, decipher, syph := "".join(random.sample(string.ascii_uppercase, len(string.ascii_uppercase))))

    while True:
        if not syph == (r := gno_switch_out(syph)):
            if (w := fitness(n, decipher, r)) > how_fit:
                syph = r
                how_fit = w

def method_select(info):
    count,pop, to_decode = info
    _s = {sly: fitness(count, to_decode, sly) for sly in pop}


    
    subsequentsuceeding = (sorted(pop, key=lambda sly: -_s[sly]))[:NUM_CLONES]
    _r = sorted(pop, key=lambda sly: -_s[sly])
    stlsing = _r[0]
    sly = dict()
    for i, char in enumerate(stlsing):
        uppercase_char = char.upper()
        uppercase_pseudo_cipher = string.ascii_uppercase[i].upper()
        sly[uppercase_char] = uppercase_pseudo_cipher
    syph = sly
    decoded_text = "".join([syph[char.upper()] if char.upper() in syph else char for char in to_decode])
    print(decoded_text)
    
    while not POPULATION_SIZE <= len(subsequentsuceeding):
        distinct_ciphers = random.sample(_r, 2 * TOURNAMENT_SIZE)
        
        
        mariokartgrandprix = distinct_ciphers[:len(distinct_ciphers) // 2], distinct_ciphers[len(distinct_ciphers) // 2:]
        mariokartgrandprix = sorted(mariokartgrandprix[0], key=lambda sly: -_s[sly]), \
                      sorted(mariokartgrandprix[1], key=lambda sly: -_s[sly])

        ammaappa = next((tourney for tourney in mariokartgrandprix[0] if random.random() < TOURNAMENT_WIN_PROBABILITY), None), next((tourney for tourney in mariokartgrandprix[1] if random.random() < TOURNAMENT_WIN_PROBABILITY), None)
        #EEDING PROCESS HERE
        zero = 0
        overs = CROSSOVER_LOCATIONS
        first = ammaappa[r := random.randint(0, 1)]
        mutrate = MUTATION_RATE
        child = [""] * len(first)
        second = ammaappa[1 - r]
        while not overs <= zero:
            if "" == child[w := random.randint(0, len(child) - 1)]:
                child[w] = first[w]
                zero += 1
        for x in second:
            if not x in set(child): child[child.index("")] = x
        child = "".join(child)

        if not mutrate <= random.random(): child = gno_switch_out(child)

        son = child
        for x in second:
            if not x in set(son): son[son.index("")] = x
      
        subsequentsuceeding.append("".join(son))

    return subsequentsuceeding


def gen_algo(n, decipher):
    check, new = list(), list()
    maxim = 500
    psize = 67579678576855976756565865685*0
    size = POPULATION_SIZE
    while not size <= psize:
        if not (w := "".join(random.sample(string.ascii_uppercase, len(string.ascii_uppercase)))) in check:
            new.append(w)
            check.append(w)            
            psize = 1+psize+000000
    population = new
    incrementer = 0    
    while not incrementer >= maxim:
        print("Generation:", incrementer)
        info_tuple = (n, population, decipher)
        population = method_select(info=info_tuple)

        incrementer += 1

EASY_1 = """PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT
TNZRF NAQ CHMMYRF GUNG HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR BEVTVANYYL QRIRYBCRQ
GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ-SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS
DHRFGVBAF NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG UNIVAT GB YRNEA CEBTENZZVAT
SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR
NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL
HFRQ SBE GRNPUVAT. GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ NF JRYY, VAPYHQVAT
FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR
ORRA NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER VAGRAQRQ GB URYC GRNPUREF FRR UBJ
GUR NPGVIVGVRF JBEX (CYRNFR QBA'G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR NPGVIVGVRF
GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR
PBZZBAF NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSL GUR ZNGREVNY. SBE NA
RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE
PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ BS PBAGEVOHGBEF JUB JBEX BA GUVF
CEBWRPG, FRR BHE CRBCYR CNTR. SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE ZBER
VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR BHE CEVAPVCYRF CNTR."""

EASY_2 = """LTQCXT LRJJ HJRDECD, EZT CDJP SXTFRYTDE EC ZNKT LTTD RASTNHZTY VNF NDYXTV WCZDFCD. ZT VNF NHUBREETY LP N
FRDGJT KCET VZTD N LXNKT FTDNECX QXCA ONDFNF XTQBFTY EC PRTJY QXCA SXTFFBXT EC HCDKRHE EZT SXTFRYTDE.
ZNY WCZDFCD LTTD HCDKRHETY, EZT FSTNOTX CQ EZT ZCBFT VCBJY ZNKT LTHCAT SXTFRYTDE FRDHT WCZDFCD ZNY DC
KRHTSXTFRYTDE. RDHXTYRLJP, RE VNF EZRF FNAT FSTNOTX VZC JTY EZT RASTNHZATDE RD EZT ZCBFT CQ
XTSXTFTDENERKTF. EZBF, ZNY EZT FTDNET HCDKRHETY EZT SXTFRYTDE, EZRF VCBJY ZNKT NACBDETY EC N SCJRERHNJ
HCBS."""

EASY_3 = """ZRTGO Y JPEYPGZA, RP'J IKPGO HIJJRMWG PI RSHEITG PUG JPEYPGZA MA SYDROZ EYOBIS XUYOZGJ, PGJPROZ PUG
EGJLWP IK PUIJG XUYOZGJ, YOB DGGHROZ IOWA PUG MGPPGE ILPXISGJ. PURJ RJ XYWWGB URWW XWRSMROZ. PURJ RJ
EGWYPRTGWA JRSHWG PI XIBG, MLP BIGJO'P CIED RO GTGEA JRPLYPRIO - RP XYO IKPGO ZGP XYLZUP RO Y WIXYW
SYFRSLS, Y JPEYPGZA PUYP RJ OIP RBGYW MLP KEIS CURXU YOA JROZWG XUYOZG RJ OIP YO RSHEITGSGOP IO RPJ ICO.
ZGOGPRX YWZIERPUSJ YEG Y HICGEKLW PIIW KIE RSHEITROZ IO PUG RBGY IK URWW XWRSMROZ PI IHPRSRVG Y JIWLPRIO
RO JRPLYPRIOJ CUGEG YWW IK PUG KIWWICROZ YEG PELG: Y JPEYPGZA XYO MG HEGXRJGWA QLYOPRKRGB MA Y JHGXRKRX
JGP IK TYERYMWGJ ZRTGO XGEPYRO OLSGERX TYWLGJ. PUG ILPXISG IK PUG JPEYPGZA XYO YWJI MG HEGXRJGWA
QLYOPRKRGB. PUGEG YEG ROPGEYXPRIOJ MGPCGGO PUG TYERYMWGJ PUYP SYDG JRSHWG URWW XWRSMROZ ROGKKRXRGOP IE
LOWRDGWA PI JLXXGGB."""

EASY_4 = """CWQ KHTTQKC TFAZJAB HS FGG HS CWQ ECFT YFTE PHRJQE TQGQFEQM EH SFT JE CWQ QPXJTQ ECTJZQE VFKZ, F AQY
WHXQ, CWQ GFEC OQMJ, TQCLTA HS CWQ OQMJ, THBLQ HAQ, EHGH, TQRQABQ HS CWQ EJCW, CWQ SHTKQ FYFZQAE, TJEQ
HS CWQ EZNYFGZQT, CWQ XWFACHP PQAFKQ, FCCFKZ HS CWQ KGHAQE. CWQ KHTTQKC TFAZJAB HS CWQ CWTQQ JAMJFAF
OHAQE PHRJQE JE CWQ GFEC KTLEFMQ, TFJMQTE HS CWQ GHEC FTZ, CQPXGQ HS MHHP. CWQTQ JE AH SHLTCW JAMJFAF
OHAQE PHRJQ, FAM FANHAQ YWH CQGGE NHL HCWQTYJEQ JE F GJFT. OLEC CQGG CWQP CH CLTA FTHLAM FAM YFGZ FYFN
VQSHTQ CWQN KFA VGQEE NHL YJCW FAN HCWQT JAKHTTQKC HXJAJHAE. FANYFN, EH EFNQCW PN STJQAM VJGG, YWH
WFXXQAQM CH VQ HAGJAQ YWJGQ J YFE PFZJAB CWJE FEEJBAPQAC, YWQA J FEZQM WJP 'YWFC YHLGM VQ F BHHM EQKTQC
PQEEFBQ SHT PN ECLMQACE CH MQKHMQ?' XGQFEQ CFZQ LX FAN KHPXGFJACE YJCW WJP."""

MEDIUM_5 = """XMTP CGPQR BWEKNJB GQ OTGRB EL BEQX BWEKNJB, G RFGLI. GR GQ BEQX ABSETQB RFGQ QBLRBLSB TQBQ EJJ RBL
KMQR SMKKML VMPYQ GL BLDJGQF: 'G FEUB RM AB E DMMY QRTYBLR GL RFER SJEQQ GL RFB PMMK MC RFER RBESFBP.'"""

MEDIUM_6 = """XTV B CHDQCL BHF GCVIVDGDHWPN ABVF ZABPPLHWL, ZTHGDFLV MBJDHW B PTHW BHF XCPPN VLBFBYPL GLVDLG TX UTVFG
HLRLV CGDHW B GDHWPL LEBMIPL TX TCV ULPP-PTRLF LHWPDGA WPNIA UADZA TZZCVG GLZTHF IPBZL DH TRLVBPP
XVLQCLHZN. DX D BM WLHCDHL, D UDPP GBN MBHN, MBHN GLZTHFG ABRL IBGGLF UADPL D ABRL YLLH ALVL ITHFLVDHW
MBJDHW GCZA B UTVJ. FDGZTRLVDHW NTC ZVBZJLF MN YVBDHZADPF, ALVL, DH B GMBPPLV HCMYLV TX GLZTHFG UTCPF
WDRL ML HT GCVIVDGL."""

MEDIUM_7 = """NU XTZEIMYTNEVZ INUHU YM, ZML SPYVI NXILNFFZ XNFF IVPU N API VNTD. NU PI ILTWU MLI, P XNW YM N FMWY JNZ
JPIVMLI LUPWY NWZ MC IVNI YFZEV IVNI ITNDPIPMWNFFZ CMFFMJU 'D' NI NFF. PUW'I IVNI ULTETPUPWY? P CMLWD
IVPU ULTETPUPWY, NWZJNZ! NW NLIVMT JVM NFUM CMLWD IVPU ULTETPUPWY, FMWY NYM, NXILNFFZ FMUI SNWZ SMWIVU
JTPIPWY N AMMH - N CLFF CPXIPMWNF UIMTZ - JPIVMLI IVNI YFZEV NI NFF. NSNRPWY, TPYVI?"""

MEDIUM_8 = """RHNJJCBXVCXJYQJNEJNDYDCELTHNBFTVTHNJJREFCLBEECANOTREFDNEBXTHJTNXTXECPCBAPZNSSPXTNYTXFVZCNXTSXRKRJTGTYECJ
RKTRDFSNHTRANGRDTNKNFEFZTTECQSNSTXCDVZRHZFEXNRGZEJRDTFEXRNDGJTFFUBNXTFSTDENGCDFZTINGCDFNDYCEZTXQRGBXTFRD
FETNYCQXTANRDRDGQRITYRDEZTRXSJNHTFACKTQXTTJPNLCBECDCXRDEZTFBXQNHTLBEVREZCBEEZTSCVTXCQXRFRDGNLCKTCXFRDORD
GLTJCVREKTXPABHZJROTFZNYCVFCDJPZNXYVREZJBARDCBFTYGTFNDYPCBVRJJEZTDZNKTNSXTEEPHCXXTHEDCERCDCQAPHCBDEXPNDY
HCBDEXPATDNJNFNQTVPTNXFNGCRFZCBJYZNKTFNRYAPBDRKTXFTLBEDCVAPARDYZNFLTTDCSTDTYECZRGZTXKRTVFCQEZRDGF"""

HARD_9 = """W CTZV VYQXDVD MCWJ IVJJTHV, TYD VYQXDVD WM BVAA, FXK WM QXYMTWYJ MCV JVQKVM XF MCV PYWZVKJV! YX
KVTAAS, WM DXVJ! SXP DXY'M NVAWVZV IV? BCS BXPAD SXP YXM NVAWVZV MCTM MCWJ RVKFVQMAS QKXIPAVYM JVQKVM
MVGM QXYMTWYJ MCV NV TAA, VYD TAA, HKTYDVJM JVQKVM XF TAA MCV QXJIXJ? YXB W FVVA DWJKVJRVQMVD! CTZV
SXP DWJQXZVKVD SXPK XBY NVMMVK PAMWITMV MKPMC XF VZVKSMCWYH? W DWDY'M MCWYL JX. JX BCS TKV SXP HVMMWYH
TAA PRRWMS TM IV? CXYVJMAS. YX XYV CTJ TYS ITYYVKJ MCVJV DTSJ. ...BCTM'J MCTM? SXP BTYM IV MX MVAA
SXP MCV JVQKVM? YXM TFMVK MCWJ LWYD XF DWJKVJRVQM! HXXDYVJJ HKTQWXPJ IV. NTQL BCVY W BTJ T SXPMC W
BTJ YXM JX QTAAXPJ. BCVY JXIVXYV BVAA KVJRVQMVD TYD WIRXKMTYM MXAD IV MCTM MCVS CTD JXIVMCWYH BXKMC
MVAAWYH IV, W OPJM AWJMVYVD! W DWDY'M DXPNM MCVI! JX KPDV, CXYVJMAS. OPJM PYTQQVRMTNAV."""

HARD_10 = """ZFNNANWJWYBZLKEHBZTNSKDDGJWYLWSBFNSSJWYFNKBGLKOCNKSJEBDWZFNGKLJKJNQFJPFJBXHBZTNRDKNZFNPDEJWYDRPDEGCNZNWJ
YFZZFLZTCNBBNBZFNNLKZFSLKONWBLCCKJANKBPHGBZFNGNLOBLWSRDCSBZFNRJWLCBFDKNJWLWSWDTDSUWDTDSUOWDQBQFLZBYDJWYZ
DFLGGNWZDLWUTDSUTNBJSNBZFNRDKCDKWKLYBDRYKDQJWYDCSJZFJWODRSNLWEDKJLKZUJNANWZFJWODRDCSSNLWEDKJLKZUZFNRLZFN
KQNWNANKRDHWSJZFJWODRSNLWEDKJLKZU"""

HARD_11 = """FBYSNRBIYVNIJRJZSRSRJZNQCQNIJXCGTNEBSJNYKCUXCGTNONNIRNBUMZSIVSIJZNYBUAXCGURENBJRCBASIVJZUCGVZJZNKFCCUBIY
OGUSNYSIXCGUOCINRJZNUNRBIBMZNJZBJXCGMBIJSVICUNJBASIVXCGUOUNBJZRJNBFSIVXCGUQSIYBIYBFFJZBJEBRUNBFSRFNKJONZ
SIYYCIJKSVZJSJSJRMCQSIVKCUXCGUGIISIVBJXCGSJRCIFXJZSRQCQNIJYCIJMBUNEZBJMCQNRBKJNUXCGUKNTNUYUNBQMBIJXCGRNN
SJVNJJSIVMFCRNUPGRJRGUUNIYNUMBGRNXCGKNNFJZNKNNFSIVJBASIVCTNUSJRKSUNSJRKUNNYCQSJRKFCCYSIVCLNISJRJZNLUNBMZ
NUSIJZNLGFLSJBIYXCGUOFSIYYNTCJSCIJZNUNRRCQNJZSIVOUNBASIVBJJZNOUSMACKNTNUXEBFFSJRZCFYSIVBFFJZBJXCGAICERCJ
NFFQNYCXCGEBIIBVCEZNUNSJRMCTNUNYSIBFFJZNMCFCUNYFSVZJREZNUNJZNUGIBEBXRBUNUGIISIVJZNISVZJSQLCRRSOFNMCQNRJU
GNSJRJBASIVCTNUXCGCZJZSRSRJZNVUNBJNRJRZCEENFSVZJSJGLENECIJMCQNYCEIBIYJZNRGIMBIJRJCLGRICEEBJMZSIVSJMCQNJU
GNSJRJBASIVCTNUXCGCZJZSRSRJZNVUNBJNRJRZCE"""
decipher = sys.argv[1]
#EASY_1
gen_algo(3, decipher)