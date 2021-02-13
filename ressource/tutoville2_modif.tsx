<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.4" tiledversion="1.4.3" name="tutoville2_modif" tilewidth="16" tileheight="16" spacing="1" margin="1" tilecount="1320" columns="60">
 <image source="tutoville2_modif.png" width="1021" height="375"/>
 <terraintypes>
  <terrain name="debut" tile="60">
   <properties>
    <property name="start" type="bool" value="true"/>
   </properties>
  </terrain>
  <terrain name="route" tile="120">
   <properties>
    <property name="canPass" type="bool" value="true"/>
   </properties>
  </terrain>
  <terrain name="arrivé" tile="180">
   <properties>
    <property name="end" type="bool" value="true"/>
   </properties>
  </terrain>
 </terraintypes>
</tileset>
