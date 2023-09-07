from test_functions import test_traj_rho
from time import time
import numpy as np

seeds = [279110,858672,921163,434124,906748,361052,197533,292182,203247,997135,
421702,297841,25053,120591,131443,27386,378812,575650,425575,432850,
252618,845964,738361,319864,259316,18327,315695,856488,652500,208623,
630365,711292,939481,930647,383172,154869,884927,971683,795923,656452,
398190,508762,175947,861511,271714,453860,464913,448185,191173,476011,
259219,865781,705956,374790,438901,875793,326784,994493,668070,372296,
653959,371016,231112,997219,892923,818461,252131,265818,984458,966976,
113064,433861,827332,888895,211943,193190,391834,41099,668980,670038,
546203,404989,685339,858772,886507,923132,124650,525353,58377,36223,
160752,304712,464352,285489,335891,686127,947262,589475,772193,589054,
459846,821694,824584,6673,225541,824212,554942,268904,502687,631822,
853903,473822,789538,324077,670072,641154,965389,787492,690484,271518,
448228,948587,161974,113498,104111,988403,266531,888851,135435,351071,
429331,408158,942675,803691,788156,452153,173033,877854,709289,849383,
785259,662854,61251,737458,889799,998427,4834,757546,55535,312358,
195448,64834,726890,528428,794456,885028,403992,138824,475239,981790,
740558,605316,507080,367981,844966,224818,193922,225841,59443,169217,
821866,563370,546284,817571,522322,253064,428045,244559,328219,172019,
442490,883843,757505,169193,914566,914528,935407,576273,417140,587078,
477508,848421,971425,540785,607464,26796,877468,917819,981842,305183,
862832,307667,231831,468114,768185,281914,25529,35354,878685,888587,
641268,736577,155112,974729,613169,198557,447103,709957,267599,953533,
802753,40557,256500,796718,946882,20139,885887,811030,253967,243970,
528952,946,552907,211511,152311,710620,290716,938890,312284,664513,
248522,767954,231908,775529,867002,172213,202855,470475,872360,854831,
971963,665279,961105,474570,139944,114573,522893,469683,681929,307120,
260761,874950,404195,995116,467007,855623,985201,900236,213217,193453,
381401,458057,490808,284956,516244,145052,778741,662656,180557,154030,
270554,346281,745484,857118,790708,514509,866872,494915,527193,318675,
600921,830134,444517,144770,834404,5221,295875,100096,318554,689250,
324257,886034,221095,59031,746584,352804,468583,577160,294487,199622,
996003,918750,828430,804110,918845,861092,133676,726197,328887,277886,
988999,991262,726200,380692,295312,474157,89884,615334,248789,497751,
601298,49936,343569,379090,893716,960529,841801,350120,919803,718792,
67214,807243,389506,539589,110857,690174,913561,825466,605263,180286,
96261,632451,16801,633613,663600,471258,672769,337967,24504,598152,
282004,197752,792720,846367,616662,891296,131158,613417,655108,231969,
388485,288202,399022,942329,480328,987265,153130,787369,235394,988682,
115311,393731,310946,631020,738930,333454,891952,861809,234525,999258,
581721,280809,915399,332612,816475,841779,973501,994770,981239,263750,
373702,375065,908687,545336,43120,856587,376599,310788,592682,415364,
769060,692249,837195,648347,808154,918727,768660,913721,227863,160685,
729962,775351,242314,865158,726798,207232,481877,665330,989830,280319,
57100,441386,197352,605869,475112,201124,20689,281920,725948,190445,
378400,70355,606551,283349,508815,580446,484992,802601,460787,541744,
638112,83716,42938,12406,855475,754383,9530,9973,135707,38685,645155,
659882,505030,883180,934047,779665,619235,475719,183425,806757,721390,
290465,41446,444827,201967,736055,784356,496916,810955,956668,768671,
742339,224036,824329,866532,675927,189908,184534,586880,153201,416889,
616872,582146,305974,986551,918153,658544,980400,613979,544705,971653,
289151,727338,278698,497489,529666,892529,439041,79929,537298,93721,
84238,232773,620713,227269,836856,714263,434026,9666,60937,974220,
435809,859660,409431,873951,326472,831085,468435,846397,94606,57463,
661849,130422,69222,784427,717452,756369,47669,931136,882400,610645,
445236,147508,379772,592413,522595,909049,552421,88057,160544,713887,
148375,630499,906938,417743,764047,945301,889746,322555,270572,46211,
780153,563391,611356,485845,229472,140725,128653,891571,71675,405223,
439885,910560,492296,36292,965502,279033,578726,617174,116156,62327,
638625,724205,621568,498068,545072,584443,490345,157759,834226,857062,
950739,357621,420833,87942,698411,1513,471427,347448,565653,289983,
663735,540257,729191,28180,459733,110023,377590,15380,717291,74281,
560679,34472,491153,245921,380436,345968,152177,819324,401942,231257,
813414,810589,829345,845651,395388,790604,737319,485123,304202,406357,
579584,975318,629894,39902,96831,760621,471283,574505,959052,399296,
119984,4241,815125,8596,975045,468904,395541,628729,190378,95065,
615393,634671,421836,955115,108203,320544,755998,945356,28596,630289,
505245,721493,428134,115476,174910,446749,967735,980480,226732,562363,
289391,108447,649524,177435,140462,231465,872770,695957,388198,247412,
76699,182060,260154,995204,182268,716057,955528,285869,583035,207784,
360452,745264,285388,124778,440719,379758,417243,265025,469939,84156,
652431,859124,944810,338318,937275,482172,707597,996996,830609,450037,
757,284319,520315,987029,269090,710508,248722,834067,43656,503899,
602845,122985,320041,150507,719232,251387,898239,100917,364442,37119,
58814,18506,728511,498007,619360,654586,191328,970065,233280,216912,
575055,106919,954133,637089,816007,864394,685725,593960,668324,860275,
106464,965814,522087,651626,703665,167884,24567,371834,746356,224704,
28515,403859,730990,210926,31920,355688,646349,440843,434792,954634,
896092,263786,686908,362087,645995,829077,785362,593499,686380,811889,
617591,456222,548705,865328,476887,416812,737303,153946,231847,204010,
702950,634036,586912,334978,71318,829952,793021,509094,275397,616465,
229275,921032,282320,288797,99961,527369,589493,313875,8346,843403,
382117,474479,227246,361302,690253,660669,805436,234164,931984,988035,
743514,203509,143704,823744,919104,295039,236766,377887,461110,217434,
96006,80521,107161,390979,682064,197008,89838,525689,95010,810562,
423796,495340,276616,764803,41632,62810,948144,310084,939761,626706,
644831,105706,546460,452280,321613,445424,724112,282888,338922,421415,
827994,243803,542392,134165,575755,467735,423518,432422,153437,352751,
95749,512075,811924,789876,929922,511995,480267,622660,623214,130615,
29191,710310,490136,439022,106643,452155,868694,145833,7258,465460,
129218,558988,317849,406537,465866,298109,259931,592194,273253,913764,
845267,909929,318095,664638,984917,682154,697240,726470,911725,774532,
146183,471964,790611,117971,644034,829446,929860,988431,685479,363178,
131739,675673,821190,72995,839673,610714,755470,416480,999305,728795,
26753,44268,266469,771336,200682,942820,740580,652907,996272,109197,
119963,867885,324331,357689,713636,307294,882426,161418,838161,791642,
920451,330460,723958,888086,178419,800600,148762,210169,345060,853371,
53339,31625,464056,566394,941702,460917,660639,595289,937314,857223,
683754,433852,655814,324812,569370,334036,285073,440413,294423,680679,
290688,704255,236968,377523,634078,253866,824185,748963,577203,788475,
732907,424461,11003,120998,707180,285492,851655,822121,721404,339461,
778,669213,868000,391764,590288,784551,136937,823071,612843,280031,
372532,598396,602051,110935,560900,585681,982857,840144,310067,335705,
369945,59409,936804,709849,440369,394739,428670,121882,558446,844380,
18012,64509,191518,566970,97000,689149,361443,696549,139577,905793,
853875,392795,241700,430688,372920,486110,926278,345339,50574,305803,
819674,781167,486490,198516,225343,259665,97468,3753,524308,320506,
155728,293307,249813,284878,290763,624316,300837,900808,921148,938848,
406860,245887,707876,39348,23790,831511,85242,108131,460745,254714,
538871,492167,200814,509632,793223,277938,306841,469347,900851,329645,
406536,796885,88590,739582,815519,20285,806461,24117,90135,288061,
246538,894105,497978,275854,394968,58178,421189,739077,911210,98118,
791651,298515,740632,828563,17348,179368,817069,675665,911740,778674,
631678,330476,831329,931579,452452,983780,666153,34224,306345,736103,
774413,940034,734027,535265,838215,823917,947287,291064,428307,151203,
276905,839606,736631,775459,737501,634648,538208,312893,778287,792046,
705903,49937,41859,5613,124808,167225,742456,609192,782558,333391,
485983,717379,813370,4898,849687,247365,562434,796160,669532,506035,
962206,504366,348764,726082,880162,616592,284703,209443,469646,616287,
688843,99616,180031,605469,603884,336771,69799,966155,684615,296766,
266302,101198,510094,418362,351174,557020,194878,306254,524264,741120,
480653,695005,82576,468284,186061,366339,240913,828361,388322,263821,
165389,353451,761786,86756,943031,206574,1742,873605,747078,175331,
323127,742174,704894,500215,343947,362086,89516,408583,58270,807014,
640429,486495,306360,486615,26629,784957,145702,163638,417803,457933,
636335,364072,320500,14395,650516,577696,78721,977822,832248,614036,
258459,803191,434852,797494,894621,103519,292065,784123,610678,477282,
26758,87256,27176,426061,203516,371243,194291,452627,708484,902394,
579015,696011,821033,496667,175346,434365,415123,744993,309139,226100,
860910,327310,951602,563406,375568,759759,804816,47712,429648,568775,
550077,633215,117466,398798,662868,236487,375653,596829,903618,84148,
702990,176855,733326,572584,134419,863162,63623,664556,385426,277668,
7220,198579,456705,888471,614842,575085,805587,193790,300404,442480,
818028,254330,246413,414184,768390,899250,861435,953329,691114,594276,
202304,627497,431688,682130,751586,598870,157797,651360,706907,180021,
107726,613721,214838,488342,28275,638510,420203,67172,937333,706683,
657295,213182,655945,288281,415445,723609,601652,278143,873827,715470,
223139,850989,841743,326530,563727,470493,418417,983044,156640,938127,
546640,268679,47505,30102,434564,885046,597771,195175,205576,826818,
20426,324721,510812,988361,986912,387507,598248,82793,740862,180980,
748491,866584,520600,253353,328738,975532,314916,397032,413750,309368,
596299,356669,345749,627566,876737,42751,107499,281440,161160,905108,
361126,612036,580717,72337,211481,512907,936544,166770,797749,569970,
853683,354263,988104,392617,327797,149257,298429,442229,167080,602611,
174176,737638,134449,696670,251457,757815,520239,437912,724083,609904,
456647,825138,176597,627168,117957,477649,862125,801671,364863,71451,
903253,830215,522249,376468,660205,224095,916577,737285,866545,803258,
345908,588477,25777,605605,569685,986755,334490,590549,559365,729681,
855166,433644,470540,73405,909196,358288,930660,363219,260582,235424,
885630,231615,892525,730027,269576,144650,872138,189518,554139,748935,
240552,114168,490895,778445,658604,137555,765827,911509,445138,752251,
685340,515113,352331,96389,755210,866484,481963,269525,593210,732318,
408944,285451,761498,162094,81751,354491,352678,998856,274948,22292,
31154,572654,830588,209910,932663,766151,381078,999696,56805,14864,
138439,213644,663385,949900,863102,402925,357037,848240,612685,193758,
635707,104066,395318,861112,441963,167912,142849,360435,218406,834373,
985712,392417,771499,800191,315652,74737,998270,118443,748545,77990,
22367,14459,82476,726065,400918,441409,452476,781949,167908,339802,
626650,851529,757958,473446,275157,165317,511663,710107,791486,675044,
701205,349729,307322,562724,782905,191721,201710,179947,620504,766025,
163005,542785,153434,408426,467429,448130,68490,968687,563813,785763,
425066,766458,991524,649928,17811,537522,986405,643149,9512,393210,
774486,17291,415033,48887,213084,178407,689379,268449,311701,784607,
103652,523146,801829,945641,32589,28262,101799,300956,324907,503740,
465587,501815,791696,869375,762562,274138,798551,134366,266652,343280,
238877,127750,914389,229841,951631,989261,312987,840467,897,301484,
691118,876468,25343,569025,655564,464161,360535,782003,942251,178816,
379637,614880,726529,832283,51531,297078,431277,676908,38598,183433,
294936,704616,409487,992329,131103,956145,258482,691946,162912,382591,
318337,710227,685185,696548,151916,909413,517805,23010,386305,581964,
906337,404048,738576,80256,543699,215875,673377,800554,239936,506503,
807152,927497,997151,832742,835267,1836,350795,677875,284128,812258,
319173,284593,44836,637024,345182,989472,471572,716685,855197,140568,
146790,39850,950054,410262,582228,458757,421619,911319,977011,504863,
305478,282363,968934,547799,168932,970430,320868,727434,590772,467471,
350894,505527,320042,168106,920444,811027,323866,751282,183095,993347,
218544,572426,136414,256610,8566,684567,524974,51224,978178,290710,
799014,706327,666652,710593,847983,44396,511023,642964,83110,334334,
900219,641662,317082,993424,256044,596237,188712,32682,533200,903272,
705658,916173,438129,415771,253174,298939,899706,389912,111028,759292,
530949,183114,219951,771654,896362,645719,961293,695680,643721,89108,
644923,51817,720007,46267,983547,815213,541840,875764,650318,101668,
104645,306898,268673,917065,92193,402859,160221,653829,36213,146641,
82343,387030,168751,726660,81662,268589,328607,552388,226395,264404,
615969,359,377249,661437,595727,45333,962964,784251,18185,540606,
84977,417175,434029,392613,503633,281052,136084,426685,815974,560891,
22597,493042,235268,424033,603867,446023,231817,496933,920302,657749,
961062,631408,425135,623084,677337,461429,154289,495288,14299,864564,
454289,772404,547638,656027,317087,452816,828324,948330,100610,2029,
304635,940041,655595,936181,966956,845152,313721,517511,330818,144264,
453946,604432,114474,617201,60744,113715,788791,508105,996725,177315,
710194,326518,534255,120517,794325,681278,716926,957372,54358,275351,
64041,877658,781192,279659,79047,68130,796398,590274,153084,523928,
345996,177438,109899,680240,794392,932012,979687,773643,830836,912330,
274086,283528,94290,891421,589293,379679,101681,450465,461985,934259,
721530,881837,162666,568632,563968,318056,665842,603235,218487,735432,
172839,954535,25153,921861,208568,718504,41423,144203,236884,108726,
33739,590303,144347,186240,472370,721106,296654,987878,529676,646818,
419849,610757,476113,36128,951407,551557,472434,269382,423801,33083,
683704,843480,647114,713102,61861,972874,686145,805521,589051,311925,
951482,106820,511041,69398,424134,525913,246416,700499,972277,561380,
383111,246804,336854,85856,907733,274263,910638,99079,40139,955927,
953177,973056,706817,46453,691956,195210,202410,127950,626827,404219,
433248,992357,178145,214923,122060,362324,892240,190135,650102,470550,
528090,311568,196324,582223,286482,591340,24894,32369,231490,719803,
514256,523367,156252,217546,192152,949399,921247,109425,569030,252807,
825855,976133,512066,936286,275919,932796,83503,387576,345335,317860,
175175,493239,981331,650638,203122,951157,849989,647483,591772,379817,
395872,632443,771553,4181,246271,513054,235907,450891,124796,710161,
619416,112070,219893,968978,333675,893519,705973,610988,616443,351123,
255601,612463,352026,733667,94914,190239,132863,127471,141681,880177,
596562,253935,264235,770539,889530,990891,671132,983675,175718,663466,
537355,132345,423479,870360,39717,777317,704781,994988,390271,356906,
741156,909129,330821,703808,57410,954079,435967,435733,32078,784098,
445287,934805,626886,189572,28381,478495,83154,631993,906626,314940,
67475,620320,985282,776665,462497,436904,183450,502149,309866,860860,
317929,223930,812034,393254,14783,189025,681087,528154,976052,498272,
741473,712366,107783,315048,992782,515586,794407,140457,896554,83155,
936056,682725,663394,142051,883649,490496,911165,489737,446275,38440,
713742,54212,20913,260491,172299,258548,58645,684741,660528,960865,
860994,775307,163467,349420]

folder_in = './data/cabspottingdata'
ms = [5000, 10000, 15000, 20000, 25000, 30000]
rhos = [0.00000005,0.0000009,0.00005,0.00025,0.0005] #[0.0001, 0.001, 0.01, 0.1, 1]
ks = [50, 75, 100, 125]
ss = [10.4,10.4,10.4,10.4,10.4]

num_rep = 50
num_rhos = len(rhos)
num_ks = len(ks)
num_mlen = len(ms)

delta_fix = 1e-10
eps_deltas = []
for j in range(num_rhos):
    s = ss[j]
    eps_delta = s/(s-1)*2.*np.sqrt(rhos[j]*np.log(2./(s+1)/delta_fix))
    assert(eps_delta/s/rhos[j]*eps_delta>=10.0)
    eps_deltas.append(eps_delta)

rho_fix = rhos[2]
eps_delta_fix = eps_deltas[2]
m_len_fix = ms[3]
    
if __name__ == '__main__':
    run_range = range(0,5)
    tick = time()
    print('Starting test_traj_rho for range '+str(run_range[0])+' - '+str(run_range[-1]))
    test_traj_rho(folder_in, num_rep, m_len_fix, rhos, eps_deltas, seeds, run_range, folder_out_prefix='./results/test_traj_rho/', delta=delta_fix, b_cont=False, b_mp=True)
    print('Finished. Time elapsed: ',time() - tick)