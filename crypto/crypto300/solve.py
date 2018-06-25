#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from libnum import n2s, xgcd, invmod
n = 303552029739268787689421034809301542668363111985448197488656603423285809555016225763507821058977191376975609612314573787148430030014978401102426346290180457645094380918591576333426636173812372946449416193133967635136948329497046720932035699306242881374653629170574541376888732480402461582716866722983695803770299355842301744494399283912359159762979974274635961976611573875536934818825542925610132556421395122301055777262562802177229272506178634122630325492174876899080153722085540119976788604275939786645770106319848807686165366996569539304747120908823654505597519971616647713951114166662291810700501111018118275233410176961734636469348235124203204134145130577525538890279384881751619815307136021730662753639447139755612989914958460173737679972680019340240434795555887059008048980208310031478812591690215353375022942428110381458613385128108872115242768135293903468683608857300743326973147004626582751679482312050023468740515408350833053825882533336460567233765353505688832265072613475683680709995436584288121440632015107692526152295970809776420786093311436754175740811154244080248787476374748432605004090718808330731360388760195905565111121494331277093420237515276837204677350020884323188865761880255671146749130841857969707181931683

e1 = 1619455979
c1 = 198715253333205140309304762885934618229717196308890027603141480980731775107348360929691664611310937503978870900195082805430374783694030256080622016431713424487244772527324022843322914415619245021182421250854444440781360638422051666613839841944782322487338599765894102041338732574012668931813897325660246967869476602808909797162902701210216869359928429288791785452635316367779426533481308013371557355393449986658731108747490355528775172926959308658280174940152832432165736439293418874425734751782857925497662265002591513393372683454767087602379380052747936562618483274958688907439693149445829031530613277130701096166928779898938460841793137793772824993304228003993183930879792632492470483669825399423456797908143494111020418710988346835166212243585055863746810963626606308385913688254166416633006118130890757463652637792926528161963258064305876815498055545713830360972308419832086946998782649756845607923863281939402203454937273620038072346575381808812583095514453536737347381024233365706099989443504975149420539758813461360142987773976973719344200937932368445461807527624932180387123416910068146569630371506530698264164327834638083283167886159722591510801422331956288691109442923649046533833838586468844563801643083794278525900495947
e2 = 2218655053
c2 = 32615591258153885532872120460212758736134886243634813235838462055254224230156978893837241333503438837560049738811019202053666852131843579969180819135918195670435646218798338878207884486439776440812589158659112670496432433764763703282993219460450070048880305140176623143541011577825923740021624574565959168129714857503384053650796471388783129123266822191328460622571825254797074278766744344449029921455396794262946102099484014268317736955668932589922820688481421252093330569923330793746274040977414382575142010484625274440120609641303636387828213766610186034348128287594747333041518241387255743495671694388224092241334375557960221929639377746330303476364413655641985978548904603860853957255975864881413562849205221262023878345647011166440806961597198047675599204037404256459922199686158595442710782206991869971191718158251760051098349825060204755675763053569921776142673198989292051093877623107211494156101936560510747801392150211993816788481683949289424910933680711155718999443532741102445391520053539886559539610597786096127192494164164228518358927737684861597150859018781114135430259903665470055196431935820328527509699402240720477154140845753960909980044365171108581262312383752579303617377411202139764854951147676135169489302612
#  print xgcd(e1, e2)
s1, s2, _ = xgcd(e1, e2)

if s1 < 0:
    s1 = -s1
    c1 = invmod(c1, n)
elif s2 < 0:
    s2 = -s2
    c2 = invmod(c2, n)

m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
#  print m
print n2s(m)
