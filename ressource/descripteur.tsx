<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.4" tiledversion="1.4.3" name="tutoville2_modif" tilewidth="16" tileheight="16" spacing="1" margin="1" tilecount="1320" columns="60">
 <editorsettings>
  <export target="descripteur..tsx" format="tsx"/>
 </editorsettings>
 <image source="descripteur.png" width="1021" height="375"/>
 <terraintypes>
  <terrain name="terre" tile="185">
   <properties>
    <property name="canPass" type="bool" value="true"/>
   </properties>
  </terrain>
  <terrain name="eau" tile="673">
   <properties>
    <property name="canPass" type="bool" value="true"/>
    <property name="vision_area" type="int" value="2"/>
   </properties>
  </terrain>
  <terrain name="start" tile="60"/>
  <terrain name="end" tile="180"/>
  <terrain name="tracé" tile="120">
   <properties>
    <property name="canPass" type="bool" value="true"/>
   </properties>
  </terrain>
  <terrain name="eau" tile="120">
   <properties>
    <property name="danger_area" type="int" value="6"/>
    <property name="profond" type="bool" value="true"/>
   </properties>
  </terrain>
  <terrain name="caillou" tile="603">
   <properties>
    <property name="canPass" type="bool" value="false"/>
    <property name="vision_area" type="int" value="2"/>
   </properties>
  </terrain>
  <terrain name="entrée_sortie" tile="932">
   <properties>
    <property name="vision_area" type="int" value="1"/>
   </properties>
  </terrain>
  <terrain name="rebort_mur" tile="949">
   <properties>
    <property name="canPass" type="bool" value="false"/>
    <property name="vision_area" type="int" value="2"/>
   </properties>
  </terrain>
  <terrain name="arbre" tile="1081">
   <properties>
    <property name="canPass" type="bool" value="false"/>
    <property name="vision_area" type="int" value="2"/>
   </properties>
  </terrain>
  <terrain name="rocher" tile="621">
   <properties>
    <property name="canPass" type="bool" value="false"/>
    <property name="danger_area" type="int" value="5"/>
    <property name="vision_area" type="int" value="4"/>
   </properties>
  </terrain>
  <terrain name="fleur" tile="945">
   <properties>
    <property name="canPass" type="bool" value="false"/>
    <property name="vision_area" type="int" value="1"/>
   </properties>
  </terrain>
  <terrain name="bouisson" tile="1081">
   <properties>
    <property name="canPass" type="bool" value="false"/>
    <property name="vision_area" type="int" value="1"/>
   </properties>
  </terrain>
  <terrain name="passerelle" tile="677">
   <properties>
    <property name="canPass" type="bool" value="true"/>
   </properties>
  </terrain>
 </terraintypes>
 <tile id="60" terrain="2,2,2,2"/>
 <tile id="63" terrain="0,0,0,0"/>
 <tile id="64" terrain="0,0,0,0"/>
 <tile id="70" terrain="0,0,0,0"/>
 <tile id="71" terrain="0,0,0,0"/>
 <tile id="77" terrain="0,0,0,0"/>
 <tile id="78" terrain="0,0,0,0"/>
 <tile id="84" terrain="0,0,0,0"/>
 <tile id="85" terrain="0,0,0,0"/>
 <tile id="91" terrain="0,0,0,0"/>
 <tile id="92" terrain="0,0,0,0"/>
 <tile id="98" terrain="0,0,0,0"/>
 <tile id="99" terrain="0,0,0,0"/>
 <tile id="105" terrain="0,0,0,0"/>
 <tile id="106" terrain="0,0,0,0"/>
 <tile id="110" terrain="1,1,1,1"/>
 <tile id="111" terrain="1,1,1,1"/>
 <tile id="112" terrain="1,1,1,1"/>
 <tile id="115" terrain="0,0,0,0"/>
 <tile id="120" terrain="4,4,4,4"/>
 <tile id="122" terrain="0,0,0,0"/>
 <tile id="123" terrain="0,0,0,0"/>
 <tile id="124" terrain="0,0,0,0"/>
 <tile id="125" terrain="0,0,0,0"/>
 <tile id="129" terrain="0,0,0,0"/>
 <tile id="130" terrain="0,0,0,0"/>
 <tile id="131" terrain="0,0,0,0"/>
 <tile id="132" terrain="0,0,0,0"/>
 <tile id="136" terrain="0,0,0,0"/>
 <tile id="137" terrain="0,0,0,0"/>
 <tile id="138" terrain="0,0,0,0"/>
 <tile id="139" terrain="0,0,0,0"/>
 <tile id="143" terrain="0,0,0,0"/>
 <tile id="144" terrain="0,0,0,0"/>
 <tile id="145" terrain="0,0,0,0"/>
 <tile id="146" terrain="0,0,0,0"/>
 <tile id="150" terrain="0,0,0,0"/>
 <tile id="151" terrain="0,0,0,0"/>
 <tile id="152" terrain="0,0,0,0"/>
 <tile id="153" terrain="0,0,0,0"/>
 <tile id="157" terrain="0,0,0,0"/>
 <tile id="158" terrain="0,0,0,0"/>
 <tile id="159" terrain="0,0,0,0"/>
 <tile id="160" terrain="0,0,0,0"/>
 <tile id="164" terrain="0,0,0,0"/>
 <tile id="165" terrain="0,0,0,0"/>
 <tile id="166" terrain="0,0,0,0"/>
 <tile id="167" terrain="0,0,0,0"/>
 <tile id="170" terrain="1,1,1,1"/>
 <tile id="171" terrain="1,1,1,1"/>
 <tile id="172" terrain="1,1,1,1"/>
 <tile id="180" terrain="3,3,3,3"/>
 <tile id="181" terrain="0,0,0,0"/>
 <tile id="182" terrain="0,0,0,0"/>
 <tile id="183" terrain="0,0,0,0"/>
 <tile id="184" terrain="0,0,0,0"/>
 <tile id="185" terrain="0,0,0,0"/>
 <tile id="186" terrain="0,0,0,0"/>
 <tile id="188" terrain="0,0,0,0"/>
 <tile id="189" terrain="0,0,0,0"/>
 <tile id="190" terrain="0,0,0,0"/>
 <tile id="191" terrain="0,0,0,0"/>
 <tile id="192" terrain="0,0,0,0"/>
 <tile id="193" terrain="0,0,0,0"/>
 <tile id="195" terrain="0,0,0,0"/>
 <tile id="196" terrain="0,0,0,0"/>
 <tile id="197" terrain="0,0,0,0"/>
 <tile id="198" terrain="0,0,0,0"/>
 <tile id="199" terrain="0,0,0,0"/>
 <tile id="200" terrain="0,0,0,0"/>
 <tile id="202" terrain="0,0,0,0"/>
 <tile id="203" terrain="0,0,0,0"/>
 <tile id="204" terrain="0,0,0,0"/>
 <tile id="205" terrain="0,0,0,0"/>
 <tile id="206" terrain="0,0,0,0"/>
 <tile id="207" terrain="0,0,0,0"/>
 <tile id="209" terrain="0,0,0,0"/>
 <tile id="210" terrain="0,0,0,0"/>
 <tile id="211" terrain="0,0,0,0"/>
 <tile id="212" terrain="0,0,0,0"/>
 <tile id="213" terrain="0,0,0,0"/>
 <tile id="214" terrain="0,0,0,0"/>
 <tile id="216" terrain="0,0,0,0"/>
 <tile id="217" terrain="0,0,0,0"/>
 <tile id="218" terrain="0,0,0,0"/>
 <tile id="219" terrain="0,0,0,0"/>
 <tile id="220" terrain="0,0,0,0"/>
 <tile id="221" terrain="0,0,0,0"/>
 <tile id="223" terrain="0,0,0,0"/>
 <tile id="224" terrain="0,0,0,0"/>
 <tile id="225" terrain="0,0,0,0"/>
 <tile id="226" terrain="0,0,0,0"/>
 <tile id="227" terrain="0,0,0,0"/>
 <tile id="228" terrain="0,0,0,0"/>
 <tile id="230" terrain="1,1,1,1"/>
 <tile id="231" terrain="1,1,1,1"/>
 <tile id="232" terrain="1,1,1,1"/>
 <tile id="234" terrain="10,10,10,10"/>
 <tile id="235" terrain="10,10,10,10"/>
 <tile id="237" terrain="9,9,9,9"/>
 <tile id="238" terrain="9,9,9,9"/>
 <tile id="241" terrain="0,0,0,0"/>
 <tile id="242" terrain="0,0,0,0"/>
 <tile id="243" terrain="0,0,0,0"/>
 <tile id="244" terrain="0,0,0,0"/>
 <tile id="245" terrain="0,0,0,0"/>
 <tile id="246" terrain="0,0,0,0"/>
 <tile id="248" terrain="0,0,0,0"/>
 <tile id="249" terrain="0,0,0,0"/>
 <tile id="250" terrain="0,0,0,0"/>
 <tile id="251" terrain="0,0,0,0"/>
 <tile id="252" terrain="0,0,0,0"/>
 <tile id="253" terrain="0,0,0,0"/>
 <tile id="255" terrain="0,0,0,0"/>
 <tile id="256" terrain="0,0,0,0"/>
 <tile id="257" terrain="0,0,0,0"/>
 <tile id="258" terrain="0,0,0,0"/>
 <tile id="259" terrain="0,0,0,0"/>
 <tile id="260" terrain="0,0,0,0"/>
 <tile id="262" terrain="0,0,0,0"/>
 <tile id="263" terrain="0,0,0,0"/>
 <tile id="264" terrain="0,0,0,0"/>
 <tile id="265" terrain="0,0,0,0"/>
 <tile id="266" terrain="0,0,0,0"/>
 <tile id="267" terrain="0,0,0,0"/>
 <tile id="269" terrain="0,0,0,0"/>
 <tile id="270" terrain="0,0,0,0"/>
 <tile id="271" terrain="0,0,0,0"/>
 <tile id="272" terrain="0,0,0,0"/>
 <tile id="273" terrain="0,0,0,0"/>
 <tile id="274" terrain="0,0,0,0"/>
 <tile id="276" terrain="0,0,0,0"/>
 <tile id="277" terrain="0,0,0,0"/>
 <tile id="278" terrain="0,0,0,0"/>
 <tile id="279" terrain="0,0,0,0"/>
 <tile id="280" terrain="0,0,0,0"/>
 <tile id="281" terrain="0,0,0,0"/>
 <tile id="283" terrain="0,0,0,0"/>
 <tile id="284" terrain="0,0,0,0"/>
 <tile id="285" terrain="0,0,0,0"/>
 <tile id="286" terrain="0,0,0,0"/>
 <tile id="287" terrain="0,0,0,0"/>
 <tile id="288" terrain="0,0,0,0"/>
 <tile id="294" terrain="10,10,10,10"/>
 <tile id="295" terrain="10,10,10,10"/>
 <tile id="297" terrain="9,9,9,9"/>
 <tile id="298" terrain="9,9,9,9"/>
 <tile id="302" terrain="0,0,0,0"/>
 <tile id="303" terrain="0,0,0,0"/>
 <tile id="304" terrain="0,0,0,0"/>
 <tile id="305" terrain="0,0,0,0"/>
 <tile id="309" terrain="0,0,0,0"/>
 <tile id="310" terrain="0,0,0,0"/>
 <tile id="311" terrain="0,0,0,0"/>
 <tile id="312" terrain="0,0,0,0"/>
 <tile id="316" terrain="0,0,0,0"/>
 <tile id="317" terrain="0,0,0,0"/>
 <tile id="318" terrain="0,0,0,0"/>
 <tile id="319" terrain="0,0,0,0"/>
 <tile id="323" terrain="0,0,0,0"/>
 <tile id="324" terrain="0,0,0,0"/>
 <tile id="325" terrain="0,0,0,0"/>
 <tile id="326" terrain="0,0,0,0"/>
 <tile id="330" terrain="0,0,0,0"/>
 <tile id="331" terrain="0,0,0,0"/>
 <tile id="332" terrain="0,0,0,0"/>
 <tile id="333" terrain="0,0,0,0"/>
 <tile id="337" terrain="0,0,0,0"/>
 <tile id="338" terrain="0,0,0,0"/>
 <tile id="339" terrain="0,0,0,0"/>
 <tile id="340" terrain="0,0,0,0"/>
 <tile id="344" terrain="0,0,0,0"/>
 <tile id="345" terrain="0,0,0,0"/>
 <tile id="346" terrain="0,0,0,0"/>
 <tile id="347" terrain="0,0,0,0"/>
 <tile id="363" terrain="0,0,0,0"/>
 <tile id="364" terrain="0,0,0,0"/>
 <tile id="370" terrain="0,0,0,0"/>
 <tile id="371" terrain="0,0,0,0"/>
 <tile id="377" terrain="0,0,0,0"/>
 <tile id="378" terrain="0,0,0,0"/>
 <tile id="384" terrain="0,0,0,0"/>
 <tile id="385" terrain="0,0,0,0"/>
 <tile id="391" terrain="0,0,0,0"/>
 <tile id="392" terrain="0,0,0,0"/>
 <tile id="398" terrain="0,0,0,0"/>
 <tile id="399" terrain="0,0,0,0"/>
 <tile id="405" terrain="0,0,0,0"/>
 <tile id="406" terrain="0,0,0,0"/>
 <tile id="410" terrain="8,8,8,8"/>
 <tile id="411" terrain="0,0,0,0"/>
 <tile id="412" terrain="0,0,0,0"/>
 <tile id="413" terrain="0,0,0,0"/>
 <tile id="414" terrain="8,8,8,8"/>
 <tile id="415" terrain="8,8,8,8"/>
 <tile id="416" terrain="0,0,0,0"/>
 <tile id="417" terrain="0,0,0,0"/>
 <tile id="418" terrain="0,0,0,0"/>
 <tile id="419" terrain="8,8,8,8"/>
 <tile id="470" terrain="8,8,8,8"/>
 <tile id="471" terrain="0,0,0,0"/>
 <tile id="472" terrain="0,0,0,0"/>
 <tile id="473" terrain="0,0,0,0"/>
 <tile id="474" terrain="8,8,8,8"/>
 <tile id="475" terrain="8,8,8,8"/>
 <tile id="476" terrain="0,0,0,0"/>
 <tile id="477" terrain="0,0,0,0"/>
 <tile id="478" terrain="0,0,0,0"/>
 <tile id="479" terrain="8,8,8,8"/>
 <tile id="481" terrain="8,8,8,8"/>
 <tile id="482" terrain="8,8,8,8"/>
 <tile id="483" terrain="8,8,8,8"/>
 <tile id="484" terrain="8,8,8,8"/>
 <tile id="485" terrain="8,8,8,8"/>
 <tile id="486" terrain="8,8,8,8"/>
 <tile id="487" terrain="8,8,8,8"/>
 <tile id="488" terrain="8,8,8,8"/>
 <tile id="489" terrain="8,8,8,8"/>
 <tile id="490" terrain="8,8,8,8"/>
 <tile id="493" terrain="1,1,1,1"/>
 <tile id="494" terrain="1,1,1,1"/>
 <tile id="495" terrain="1,1,1,1"/>
 <tile id="496" terrain="1,1,1,1"/>
 <tile id="497" terrain="1,1,1,1"/>
 <tile id="498" terrain="1,1,1,1"/>
 <tile id="499" terrain="1,1,1,1"/>
 <tile id="500" terrain="1,1,1,1"/>
 <tile id="501" terrain="1,1,1,1"/>
 <tile id="502" terrain="1,1,1,1"/>
 <tile id="503" terrain="1,1,1,1"/>
 <tile id="506" terrain="1,1,1,1"/>
 <tile id="507" terrain="1,1,1,1"/>
 <tile id="508" terrain="1,1,1,1"/>
 <tile id="509" terrain="1,1,1,1"/>
 <tile id="510" terrain="1,1,1,1"/>
 <tile id="511" terrain="1,1,1,1"/>
 <tile id="512" terrain="1,1,1,1"/>
 <tile id="514" terrain="8,8,8,8"/>
 <tile id="515" terrain="0,0,0,0"/>
 <tile id="516" terrain="0,0,0,0"/>
 <tile id="517" terrain="0,0,0,0"/>
 <tile id="518" terrain="0,0,0,0"/>
 <tile id="519" terrain="0,0,0,0"/>
 <tile id="520" terrain="8,8,8,8"/>
 <tile id="521" terrain="0,0,0,0"/>
 <tile id="522" terrain="0,0,0,0"/>
 <tile id="523" terrain="8,8,8,8"/>
 <tile id="524" terrain="8,8,8,8"/>
 <tile id="525" terrain="8,8,8,8"/>
 <tile id="526" terrain="8,8,8,8"/>
 <tile id="527" terrain="8,8,8,8"/>
 <tile id="530" terrain="8,8,8,8"/>
 <tile id="531" terrain="0,0,0,0"/>
 <tile id="532" terrain="0,0,0,0"/>
 <tile id="533" terrain="0,0,0,0"/>
 <tile id="534" terrain="8,8,8,8"/>
 <tile id="535" terrain="8,8,8,8"/>
 <tile id="536" terrain="0,0,0,0"/>
 <tile id="537" terrain="0,0,0,0"/>
 <tile id="538" terrain="0,0,0,0"/>
 <tile id="539" terrain="8,8,8,8"/>
 <tile id="541" terrain="8,8,8,8"/>
 <tile id="542" terrain="0,0,0,0"/>
 <tile id="543" terrain="0,0,0,0"/>
 <tile id="544" terrain="0,0,0,0"/>
 <tile id="545" terrain="8,8,8,8"/>
 <tile id="546" terrain="0,0,0,0"/>
 <tile id="547" terrain="0,0,0,0"/>
 <tile id="548" terrain="0,0,0,0"/>
 <tile id="549" terrain="8,8,8,8"/>
 <tile id="550" terrain="8,8,8,8"/>
 <tile id="552" terrain="1,1,1,1"/>
 <tile id="553" terrain="1,1,1,1"/>
 <tile id="554" terrain="6,6,6,6"/>
 <tile id="555" terrain="6,6,6,6"/>
 <tile id="556" terrain="6,6,6,6"/>
 <tile id="557" terrain="6,6,6,6"/>
 <tile id="558" terrain="13,13,13,13"/>
 <tile id="559" terrain="13,13,13,13"/>
 <tile id="560" terrain="10,10,10,10"/>
 <tile id="561" terrain="10,10,10,10"/>
 <tile id="562" terrain="1,1,1,1"/>
 <tile id="563" terrain="1,1,1,1"/>
 <tile id="564" terrain="1,1,1,1"/>
 <tile id="566" terrain="1,1,1,1"/>
 <tile id="567" terrain="1,1,1,1"/>
 <tile id="568" terrain="1,1,1,1"/>
 <tile id="569" terrain="1,1,1,1"/>
 <tile id="570" terrain="1,1,1,1"/>
 <tile id="571" terrain="1,1,1,1"/>
 <tile id="572" terrain="1,1,1,1"/>
 <tile id="574" terrain="8,8,8,8"/>
 <tile id="575" terrain="0,0,0,0"/>
 <tile id="576" terrain="0,0,0,0"/>
 <tile id="577" terrain="0,0,0,0"/>
 <tile id="578" terrain="0,0,0,0"/>
 <tile id="579" terrain="0,0,0,0"/>
 <tile id="580" terrain="8,8,8,8"/>
 <tile id="581" terrain="8,8,8,8"/>
 <tile id="582" terrain="0,0,0,0"/>
 <tile id="583" terrain="8,8,8,8"/>
 <tile id="584" terrain="6,6,6,6"/>
 <tile id="585" terrain="0,0,0,0"/>
 <tile id="586" terrain="0,0,0,0"/>
 <tile id="587" terrain="0,0,0,0"/>
 <tile id="590" terrain="8,8,8,8"/>
 <tile id="591" terrain="8,8,8,8"/>
 <tile id="592" terrain="8,8,8,8"/>
 <tile id="593" terrain="8,8,8,8"/>
 <tile id="594" terrain="8,8,8,8"/>
 <tile id="595" terrain="8,8,8,8"/>
 <tile id="596" terrain="8,8,8,8"/>
 <tile id="597" terrain="8,8,8,8"/>
 <tile id="598" terrain="8,8,8,8"/>
 <tile id="599" terrain="8,8,8,8"/>
 <tile id="601" terrain="7,7,7,7"/>
 <tile id="602" terrain="0,0,0,0"/>
 <tile id="603" terrain="6,6,6,6"/>
 <tile id="604" terrain="0,0,0,0"/>
 <tile id="605" terrain="8,8,8,8"/>
 <tile id="606" terrain="0,0,0,0"/>
 <tile id="607" terrain="0,0,0,0"/>
 <tile id="608" terrain="0,0,0,0"/>
 <tile id="609" terrain="8,8,8,8"/>
 <tile id="610" terrain="8,8,8,8"/>
 <tile id="612" terrain="1,1,1,1"/>
 <tile id="613" terrain="1,1,1,1"/>
 <tile id="614" terrain="6,6,6,6"/>
 <tile id="615" terrain="6,6,6,6"/>
 <tile id="616" terrain="6,6,6,6"/>
 <tile id="617" terrain="6,6,6,6"/>
 <tile id="618" terrain="13,13,13,13"/>
 <tile id="619" terrain="13,13,13,13"/>
 <tile id="620" terrain="10,10,10,10"/>
 <tile id="621" terrain="10,10,10,10"/>
 <tile id="622" terrain="1,1,1,1"/>
 <tile id="623" terrain="1,1,1,1"/>
 <tile id="624" terrain="1,1,1,1"/>
 <tile id="626" terrain="1,1,1,1"/>
 <tile id="627" terrain="1,1,1,1"/>
 <tile id="628" terrain="1,1,1,1"/>
 <tile id="629" terrain="1,1,1,1"/>
 <tile id="630" terrain="1,1,1,1"/>
 <tile id="631" terrain="1,1,1,1"/>
 <tile id="632" terrain="1,1,1,1"/>
 <tile id="634" terrain="8,8,8,8"/>
 <tile id="635" terrain="0,0,0,0"/>
 <tile id="636" terrain="0,0,0,0"/>
 <tile id="637" terrain="0,0,0,0"/>
 <tile id="638" terrain="0,0,0,0"/>
 <tile id="639" terrain="0,0,0,0"/>
 <tile id="640" terrain="8,8,8,8"/>
 <tile id="641" terrain="8,8,8,8"/>
 <tile id="642" terrain="0,0,0,0"/>
 <tile id="643" terrain="8,8,8,8"/>
 <tile id="644" terrain="6,6,6,6"/>
 <tile id="645" terrain="7,7,7,7"/>
 <tile id="646" terrain="7,7,7,7"/>
 <tile id="661" terrain="8,8,8,8"/>
 <tile id="662" terrain="0,0,0,0"/>
 <tile id="663" terrain="6,6,6,6"/>
 <tile id="664" terrain="0,0,0,0"/>
 <tile id="665" terrain="8,8,8,8"/>
 <tile id="666" terrain="8,8,8,8"/>
 <tile id="667" terrain="7,7,7,7"/>
 <tile id="668" terrain="7,7,7,7"/>
 <tile id="669" terrain="8,8,8,8"/>
 <tile id="670" terrain="8,8,8,8"/>
 <tile id="672" terrain="1,1,1,1"/>
 <tile id="673" terrain="1,1,1,1"/>
 <tile id="674" terrain="13,13,13,13"/>
 <tile id="675" terrain="13,13,13,13"/>
 <tile id="676" terrain="13,13,13,13"/>
 <tile id="677" terrain="13,13,13,13"/>
 <tile id="678" terrain="13,13,13,13"/>
 <tile id="679" terrain="13,13,13,13"/>
 <tile id="680" terrain="13,13,13,13"/>
 <tile id="681" terrain="13,13,13,13"/>
 <tile id="682" terrain="13,13,13,13"/>
 <tile id="683" terrain="13,13,13,13"/>
 <tile id="684" terrain="1,1,1,1"/>
 <tile id="686" terrain="1,1,1,1"/>
 <tile id="687" terrain="1,1,1,1"/>
 <tile id="688" terrain="1,1,1,1"/>
 <tile id="689" terrain="1,1,1,1"/>
 <tile id="690" terrain="1,1,1,1"/>
 <tile id="691" terrain="1,1,1,1"/>
 <tile id="692" terrain="1,1,1,1"/>
 <tile id="694" terrain="8,8,8,8"/>
 <tile id="695" terrain="7,7,7,7"/>
 <tile id="696" terrain="7,7,7,7"/>
 <tile id="697" terrain="7,7,7,7"/>
 <tile id="698" terrain="8,8,8,8"/>
 <tile id="699" terrain="8,8,8,8"/>
 <tile id="700" terrain="8,8,8,8"/>
 <tile id="701" terrain="8,8,8,8"/>
 <tile id="703" terrain="8,8,8,8"/>
 <tile id="706" terrain="7,7,7,7"/>
 <tile id="707" terrain="7,7,7,7"/>
 <tile id="712" terrain="0,0,0,0"/>
 <tile id="713" terrain="0,0,0,0"/>
 <tile id="714" terrain="0,0,0,0"/>
 <tile id="717" terrain="0,0,0,0"/>
 <tile id="718" terrain="0,0,0,0"/>
 <tile id="721" terrain="8,8,8,8"/>
 <tile id="722" terrain="0,0,0,0"/>
 <tile id="723" terrain="0,0,0,0"/>
 <tile id="724" terrain="0,0,0,0"/>
 <tile id="725" terrain="0,0,0,0"/>
 <tile id="726" terrain="0,0,0,0"/>
 <tile id="727" terrain="0,0,0,0"/>
 <tile id="728" terrain="0,0,0,0"/>
 <tile id="729" terrain="0,0,0,0"/>
 <tile id="730" terrain="8,8,8,8"/>
 <tile id="732" terrain="1,1,1,1"/>
 <tile id="733" terrain="1,1,1,1"/>
 <tile id="734" terrain="13,13,13,13"/>
 <tile id="735" terrain="13,13,13,13"/>
 <tile id="736" terrain="13,13,13,13"/>
 <tile id="737" terrain="13,13,13,13"/>
 <tile id="738" terrain="13,13,13,13"/>
 <tile id="739" terrain="13,13,13,13"/>
 <tile id="740" terrain="13,13,13,13"/>
 <tile id="741" terrain="13,13,13,13"/>
 <tile id="742" terrain="13,13,13,13"/>
 <tile id="743" terrain="13,13,13,13"/>
 <tile id="744" terrain="1,1,1,1"/>
 <tile id="750" terrain="1,1,1,1"/>
 <tile id="751" terrain="1,1,1,1"/>
 <tile id="752" terrain="1,1,1,1"/>
 <tile id="761" terrain="8,8,8,8"/>
 <tile id="762" terrain="7,7,7,7"/>
 <tile id="763" terrain="8,8,8,8"/>
 <tile id="769" terrain="8,8,8,8"/>
 <tile id="770" terrain="8,8,8,8"/>
 <tile id="772" terrain="0,0,0,0"/>
 <tile id="773" terrain="0,0,0,0"/>
 <tile id="774" terrain="0,0,0,0"/>
 <tile id="775" terrain="7,7,7,7"/>
 <tile id="776" terrain="6,6,6,6"/>
 <tile id="777" terrain="0,0,0,0"/>
 <tile id="778" terrain="0,0,0,0"/>
 <tile id="781" terrain="8,8,8,8"/>
 <tile id="782" terrain="0,0,0,0"/>
 <tile id="783" terrain="0,0,0,0"/>
 <tile id="784" terrain="0,0,0,0"/>
 <tile id="785" terrain="0,0,0,0"/>
 <tile id="786" terrain="0,0,0,0"/>
 <tile id="787" terrain="0,0,0,0"/>
 <tile id="788" terrain="0,0,0,0"/>
 <tile id="789" terrain="0,0,0,0"/>
 <tile id="790" terrain="8,8,8,8"/>
 <tile id="792" terrain="1,1,1,1"/>
 <tile id="793" terrain="1,1,1,1"/>
 <tile id="794" terrain="1,1,1,1"/>
 <tile id="795" terrain="1,1,1,1"/>
 <tile id="796" terrain="1,1,1,1"/>
 <tile id="797" terrain="1,1,1,1"/>
 <tile id="798" terrain="13,13,13,13"/>
 <tile id="799" terrain="13,13,13,13"/>
 <tile id="800" terrain="1,1,1,1"/>
 <tile id="801" terrain="1,1,1,1"/>
 <tile id="802" terrain="1,1,1,1"/>
 <tile id="803" terrain="1,1,1,1"/>
 <tile id="804" terrain="1,1,1,1"/>
 <tile id="827" terrain="7,7,7,7"/>
 <tile id="828" terrain="8,8,8,8"/>
 <tile id="829" terrain="0,0,0,0"/>
 <tile id="830" terrain="8,8,8,8"/>
 <tile id="832" terrain="0,0,0,0"/>
 <tile id="833" terrain="0,0,0,0"/>
 <tile id="834" terrain="0,0,0,0"/>
 <tile id="835" terrain="8,8,8,8"/>
 <tile id="836" terrain="0,0,0,0"/>
 <tile id="837" terrain="0,0,0,0"/>
 <tile id="838" terrain="8,8,8,8"/>
 <tile id="841" terrain="8,8,8,8"/>
 <tile id="842" terrain="0,0,0,0"/>
 <tile id="843" terrain="0,0,0,0"/>
 <tile id="844" terrain="0,0,0,0"/>
 <tile id="845" terrain="0,0,0,0"/>
 <tile id="846" terrain="0,0,0,0"/>
 <tile id="847" terrain="0,0,0,0"/>
 <tile id="848" terrain="0,0,0,0"/>
 <tile id="849" terrain="0,0,0,0"/>
 <tile id="850" terrain="8,8,8,8"/>
 <tile id="853" terrain="1,1,1,1"/>
 <tile id="854" terrain="1,1,1,1"/>
 <tile id="855" terrain="1,1,1,1"/>
 <tile id="856" terrain="1,1,1,1"/>
 <tile id="857" terrain="1,1,1,1"/>
 <tile id="858" terrain="1,1,1,1"/>
 <tile id="859" terrain="1,1,1,1"/>
 <tile id="860" terrain="1,1,1,1"/>
 <tile id="861" terrain="1,1,1,1"/>
 <tile id="862" terrain="1,1,1,1"/>
 <tile id="863" terrain="1,1,1,1"/>
 <tile id="866" terrain="0,0,0,0"/>
 <tile id="867" terrain="0,0,0,0"/>
 <tile id="868" terrain="0,0,0,0"/>
 <tile id="871" terrain="0,0,0,0"/>
 <tile id="872" terrain="7,7,7,7"/>
 <tile id="873" terrain="6,6,6,6"/>
 <tile id="874" terrain="8,8,8,8"/>
 <tile id="875" terrain="8,8,8,8"/>
 <tile id="876" terrain="8,8,8,8"/>
 <tile id="877" terrain="8,8,8,8"/>
 <tile id="879" terrain="9,9,9,9"/>
 <tile id="880" terrain="0,0,0,0"/>
 <tile id="881" terrain="0,0,0,0"/>
 <tile id="883" terrain="0,0,0,0"/>
 <tile id="884" terrain="0,0,0,0"/>
 <tile id="885" terrain="9,9,9,9"/>
 <tile id="887" terrain="0,0,0,0"/>
 <tile id="888" terrain="8,8,8,8"/>
 <tile id="889" terrain="0,0,0,0"/>
 <tile id="890" terrain="8,8,8,8"/>
 <tile id="892" terrain="0,0,0,0"/>
 <tile id="893" terrain="0,0,0,0"/>
 <tile id="894" terrain="6,6,6,6"/>
 <tile id="895" terrain="8,8,8,8"/>
 <tile id="896" terrain="0,0,0,0"/>
 <tile id="897" terrain="0,0,0,0"/>
 <tile id="898" terrain="8,8,8,8"/>
 <tile id="901" terrain="8,8,8,8"/>
 <tile id="902" terrain="8,8,8,8"/>
 <tile id="903" terrain="8,8,8,8"/>
 <tile id="904" terrain="8,8,8,8"/>
 <tile id="905" terrain="7,7,7,7"/>
 <tile id="906" terrain="8,8,8,8"/>
 <tile id="907" terrain="8,8,8,8"/>
 <tile id="908" terrain="8,8,8,8"/>
 <tile id="909" terrain="8,8,8,8"/>
 <tile id="910" terrain="8,8,8,8"/>
 <tile id="926" terrain="0,0,0,0"/>
 <tile id="927" terrain="0,0,0,0"/>
 <tile id="928" terrain="0,0,0,0"/>
 <tile id="929" terrain="0,0,0,0"/>
 <tile id="930" terrain="0,0,0,0"/>
 <tile id="931" terrain="6,6,6,6"/>
 <tile id="932" terrain="7,7,7,7"/>
 <tile id="933" terrain="6,6,6,6"/>
 <tile id="934" terrain="0,0,0,0"/>
 <tile id="935" terrain="0,0,0,0"/>
 <tile id="936" terrain="0,0,0,0"/>
 <tile id="937" terrain="0,0,0,0"/>
 <tile id="939" terrain="11,11,11,11"/>
 <tile id="940" terrain="0,0,0,0"/>
 <tile id="941" terrain="0,0,0,0"/>
 <tile id="943" terrain="0,0,0,0"/>
 <tile id="944" terrain="0,0,0,0"/>
 <tile id="945" terrain="11,11,11,11"/>
 <tile id="947" terrain="0,0,0,0"/>
 <tile id="948" terrain="8,8,8,8"/>
 <tile id="949" terrain="8,8,8,8"/>
 <tile id="950" terrain="8,8,8,8"/>
 <tile id="953" terrain="0,0,0,0"/>
 <tile id="954" terrain="0,0,0,0"/>
 <tile id="955" terrain="8,8,8,8"/>
 <tile id="956" terrain="0,0,0,0"/>
 <tile id="957" terrain="0,0,0,0"/>
 <tile id="958" terrain="8,8,8,8"/>
 <tile id="963" terrain="9,9,9,9"/>
 <tile id="980" terrain="5,5,5,5"/>
 <tile id="981" terrain="5,5,5,5"/>
 <tile id="982" terrain="5,5,5,5"/>
 <tile id="986" terrain="0,0,0,0"/>
 <tile id="987" terrain="0,0,0,0"/>
 <tile id="988" terrain="0,0,0,0"/>
 <tile id="989" terrain="0,0,0,0"/>
 <tile id="990" terrain="0,0,0,0"/>
 <tile id="991" terrain="6,6,6,6"/>
 <tile id="992" terrain="6,6,6,6"/>
 <tile id="993" terrain="8,8,8,8"/>
 <tile id="994" terrain="0,0,0,0"/>
 <tile id="995" terrain="8,8,8,8"/>
 <tile id="996" terrain="7,7,7,7"/>
 <tile id="997" terrain="0,0,0,0"/>
 <tile id="1012" terrain="8,8,8,8"/>
 <tile id="1013" terrain="8,8,8,8"/>
 <tile id="1014" terrain="8,8,8,8"/>
 <tile id="1015" terrain="8,8,8,8"/>
 <tile id="1016" terrain="8,8,8,8"/>
 <tile id="1017" terrain="8,8,8,8"/>
 <tile id="1018" terrain="8,8,8,8"/>
 <tile id="1023" terrain="9,9,9,9"/>
 <tile id="1025" terrain="0,0,0,0"/>
 <tile id="1026" terrain="0,0,0,0"/>
 <tile id="1027" terrain="0,0,0,0"/>
 <tile id="1028" terrain="9,9,9,9"/>
 <tile id="1029" terrain="9,9,9,9"/>
 <tile id="1030" terrain="9,9,9,9"/>
 <tile id="1032" terrain="0,0,0,0"/>
 <tile id="1033" terrain="0,0,0,0"/>
 <tile id="1034" terrain="0,0,0,0"/>
 <tile id="1035" terrain="9,9,9,9"/>
 <tile id="1036" terrain="9,9,9,9"/>
 <tile id="1037" terrain="9,9,9,9"/>
 <tile id="1040" terrain="5,5,5,5"/>
 <tile id="1041" terrain="5,5,5,5"/>
 <tile id="1042" terrain="5,5,5,5"/>
 <tile id="1049" terrain="0,0,0,0"/>
 <tile id="1050" terrain="0,0,0,0"/>
 <tile id="1051" terrain="6,6,6,6"/>
 <tile id="1053" terrain="8,8,8,8"/>
 <tile id="1054" terrain="0,0,0,0"/>
 <tile id="1055" terrain="8,8,8,8"/>
 <tile id="1081" terrain="12,12,12,12"/>
 <tile id="1083" terrain="9,9,9,9"/>
 <tile id="1085" terrain="9,9,9,9"/>
 <tile id="1086" terrain="9,9,9,9"/>
 <tile id="1087" terrain="9,9,9,9"/>
 <tile id="1088" terrain="9,9,9,9"/>
 <tile id="1089" terrain="9,9,9,9"/>
 <tile id="1090" terrain="9,9,9,9"/>
 <tile id="1092" terrain="9,9,9,9"/>
 <tile id="1093" terrain="9,9,9,9"/>
 <tile id="1094" terrain="9,9,9,9"/>
 <tile id="1095" terrain="9,9,9,9"/>
 <tile id="1096" terrain="9,9,9,9"/>
 <tile id="1097" terrain="9,9,9,9"/>
 <tile id="1100" terrain="5,5,5,5"/>
 <tile id="1101" terrain="5,5,5,5"/>
 <tile id="1102" terrain="5,5,5,5"/>
 <tile id="1109" terrain="7,7,7,7"/>
 <tile id="1110" terrain="8,8,8,8"/>
 <tile id="1111" terrain="8,8,8,8"/>
 <tile id="1112" terrain="8,8,8,8"/>
 <tile id="1113" terrain="8,8,8,8"/>
 <tile id="1114" terrain="8,8,8,8"/>
 <tile id="1115" terrain="8,8,8,8"/>
 <tile id="1145" terrain="9,9,9,9"/>
 <tile id="1146" terrain="9,9,9,9"/>
 <tile id="1147" terrain="9,9,9,9"/>
 <tile id="1148" terrain="9,9,9,9"/>
 <tile id="1149" terrain="9,9,9,9"/>
 <tile id="1150" terrain="9,9,9,9"/>
 <tile id="1152" terrain="9,9,9,9"/>
 <tile id="1153" terrain="9,9,9,9"/>
 <tile id="1154" terrain="9,9,9,9"/>
 <tile id="1155" terrain="9,9,9,9"/>
 <tile id="1156" terrain="9,9,9,9"/>
 <tile id="1157" terrain="9,9,9,9"/>
 <tile id="1174" terrain="8,8,8,8"/>
 <tile id="1175" terrain="7,7,7,7"/>
 <tile id="1176" terrain="8,8,8,8"/>
 <tile id="1201" terrain="12,12,12,12"/>
 <tile id="1202" terrain="12,12,12,12"/>
 <tile id="1203" terrain="12,12,12,12"/>
 <tile id="1205" terrain="0,0,0,0"/>
 <tile id="1206" terrain="0,0,0,0"/>
 <tile id="1207" terrain="0,0,0,0"/>
 <tile id="1208" terrain="9,9,9,9"/>
 <tile id="1209" terrain="9,9,9,9"/>
 <tile id="1210" terrain="9,9,9,9"/>
 <tile id="1212" terrain="0,0,0,0"/>
 <tile id="1213" terrain="0,0,0,0"/>
 <tile id="1214" terrain="0,0,0,0"/>
 <tile id="1215" terrain="9,9,9,9"/>
 <tile id="1216" terrain="9,9,9,9"/>
 <tile id="1217" terrain="9,9,9,9"/>
 <tile id="1220" terrain="8,8,8,8"/>
 <tile id="1221" terrain="8,8,8,8"/>
 <tile id="1222" terrain="8,8,8,8"/>
</tileset>
