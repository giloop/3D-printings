3D-printings
============

Automate your 3D printgs with Openscad and Python
----------------------------------------------------------
These 3D prints were autoated with Openscad and Python
[Firstname plates automatically generated](http://gilles.gonon.free.fr/wp-content/uploads/PlaquesPrenomsLow.jpg)

My wife asked me if I could print the fisrtnames of the 23 pupils for her class on individual plates. 
Of course it is possible, but I soon realised that it would be quite time consuming to edit 23 times the Openscad script
generate STL files, assemble them in Slic3r ... 
So I decided to automate the whole process: Here are the script and method used, quite simple in the end !

Let's start with a simple Openscad script to generate a the name on a plate. Choose a "stencil" font (there are plenty of free fonts, I choosed [StardosStencil-Bold.ttf](http://www.fontspace.com/new-typography/stardos-stencil)),
and set the firstname as a paramter of the script. 
```cpp
</usr/share/fonts/truetype/stardos-stencil/StardosStencil-Bold.ttf>;
 prenom = "Kéziah";
 font = "StardosStencil";  // "Liberation Sans";
 style = ""; // ":style=Bold";
 lCadre = 65;
 hCadre = 20;
 difference() {
    translate([lCadre/2-5, hCadre/2-5, 1]) roundedBox(lCadre, hCadre, 2, 3);
    translate([0,0, -0.5]) linear_extrude(height = 3) text(prenom, size = 11, font = str(font, style), $fn = 20);
 }

module roundedBox(x,y,z,rad){
  hull() {
     translate([-x/2+rad, y/2-rad,-z/2]) cylinder(h=z,r=rad, $fn=50);
     translate([ x/2-rad, y/2-rad,-z/2]) cylinder(h=z,r=rad, $fn=50);
     translate([-x/2+rad,-y/2+rad,-z/2]) cylinder(h=z,r=rad, $fn=50);
     translate([ x/2-rad,-y/2+rad,-z/2]) cylinder(h=z,r=rad, $fn=50); 
  }
 }

```
![An example of a generated plate](http://gilles.gonon.free.fr/wp-content/uploads/PlaquePrenomRender.png)

An interesting feature of Openscad is that you can call it from the command line to generate a STL, setting a variable, with the following syntax :
```bash
    openscad -o Mickaël.stl -D "prenom=\"Mickaël\"" PlaquePrenom.scad
```

[caption id="attachment_332" align="aligncenter" width="300"]<a href=""><img class="size-medium wp-image-332" alt="Plaque de prénom créée avec Openscad" src="http://gilles.gonon.free.fr/wp-content/uploads/PlaquePrenomRender-300x182.png" width="300" height="182" /></a> Plaque de prénom créée avec Openscad[/caption]

L'appel d'Openscad en ligne de commande en passant une variable est donné en exemple ci-dessous. On génère un fichier STL customisé sans ouvrir Openscad. Un customizer à pas cher !
<pre></pre>
Il suffit alors de faire un script python qui automatise les appels à Openscad pour faire un fichier STL par prénom. Il est ensuite possible de créer un script Openscad qui place les plaques générées en grille pour les imprimer en 3D. Si votre imprimante est connectée à votre PC, il est possible d'automatiser toute la chaîne...

On aurait pu faire une boucle directement dans Openscad pour créer la grille, mais la solution Python présente l'avantage de pouvoir générer plusieurs fichiers STL, car dans mon cas il me fallait 2 grilles de 12 prénoms pour faire rentrer les 23 enfants de la classe.

Pour résumer, le script python :
<ul>
	<li>crée un fichier STL par prénom (élément d'une liste Python) en appelant Openscad. Les prénoms peuvent être encodés en UTF-8 avec accents,</li>
	<li>crée N scripts Openscad qui rassemblent les fichiers STL et les placent en grille, 12 fichiers par script : Assemblage-1.scad, Assemblage-2.scad, ...</li>
	<li>génère les fichiers STL des grilles pour impression 3D en appelant Openscad.</li>
</ul>
[caption id="attachment_338" align="aligncenter" width="300"]<a href="http://gilles.gonon.free.fr/wp-content/uploads/Assemblages-1et-2.png"><img class="size-medium wp-image-338" alt="Assemblages des fichiers STL pour impressions 3D" src="http://gilles.gonon.free.fr/wp-content/uploads/Assemblages-1et-2-300x122.png" width="300" height="122" /></a> Assemblages des fichiers STL pour impressions 3D[/caption]

&nbsp;

Télécharger les <a title="Codes python et openscad pour générer les plaques des prénoms" href="http://gilles.gonon.free.fr/wp-content/uploads/PlaquesPrenoms-codes-openscad-python.zip" target="_blank">codes des fichiers Python et Openscad</a> servant à générer l'ensemble.

[caption id="attachment_335" align="aligncenter" width="437"]<a href="http://gilles.gonon.free.fr/wp-content/uploads/PlaquesPrenomsLow.jpg"><img class="size-full wp-image-335" alt="Un extrait du résultat final imprimé" src="http://gilles.gonon.free.fr/wp-content/uploads/PlaquesPrenomsLow.jpg" width="437" height="651" /></a> Un extrait du résultat final imprimé[/caption]
