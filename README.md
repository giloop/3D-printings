3D-printings
============

Automate your 3D printings with Openscad and Python
----------------------------------------------------------
These 3D prints were automated with Openscad and Python: 

![alt text](http://gilles.gonon.free.fr/wp-content/uploads/PlaquesPrenomsLow.jpg "Firstname plates automatically generated")

My wife asked me if I could print the fisrtnames of the 23 pupils for her class on individual plates. 
Of course it is possible, but I soon realised that it would be quite time consuming to edit 23 times the Openscad script
generate STL files, assemble them in Slic3r ... 
So I decided to automate the whole process: here are the script and method used, quite simple in the end !

Let's start with a simple Openscad script to generate a the name on a plate. Choose a "stencil" font (there are plenty of free fonts, I choosed [StardosStencil-Bold.ttf](http://www.fontspace.com/new-typography/stardos-stencil)),
and set the firstname as a paramter of the script. 
```cpp
use </usr/share/fonts/truetype/stardos-stencil/StardosStencil-Bold.ttf>;
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

It is then simple to automate the calls to Openscad for each firstname in a Python script that:
* create a STL file for each firstname (in a Python list) by calling openscad. I struggled a bit to have firstname encoded in UTF-8 so I had to choose specific imports,
* Create N openscad scripts that gathers the firstnames in grids of STL files, 12 files per grid :
  * Assemblage-1.scad, Assemblage-2.scad, ...
* export the generated script to STL files with Openscad ready for 3D printing.

This gives : 
![alt text](http://gilles.gonon.free.fr/wp-content/uploads/Assemblages-1et-2.png "Assembling STL files fr 3D printing")

An example of "grid gathering" script generated with Openscad is:
```cpp
union() {
 	translate([0,0,0]) import("Nathan.stl");
	translate([0,25,0]) import("Margot.stl");
	translate([0,50,0]) import("Erika.stl");
	translate([0,75,0]) import("Naoma.stl");
	translate([0,100,0]) import("Yaniss.stl");
	translate([0,125,0]) import("Baptiste.stl");
	translate([70,0,0]) import("Jules.stl");
	translate([70,25,0]) import("Neil.stl");
	translate([70,50,0]) import("Ines.stl");
	translate([70,75,0]) import("Lucas.stl");
	translate([70,100,0]) import("Axel.stl");
	translate([70,125,0]) import("Jeanne.stl");
}
```

Notes :
-------
The scripts were written and tested under Linux. You will have to make minor changes to make it work under windows : the name of te font in the openscad script, and the path to the openscad exe in the Python script. 

I just tested quickly under Windows and couldn't get unicode first names working (no accents). Any help appreciated.
