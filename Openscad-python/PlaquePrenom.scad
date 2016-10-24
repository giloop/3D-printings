use </usr/share/fonts/truetype/stardos-stencil/StardosStencil-Bold.ttf>;
prenom = "Kéziah";
font = "StardosStencil";  // "Liberation Sans";
style = ""; // ":style=Bold";
lCadre = 65;
hCadre = 20;
difference() {
    translate([lCadre/2-5, hCadre/2-5, 1]) 
       roundedBox(lCadre, hCadre, 2, 3);
    translate([0,0, -0.5]) linear_extrude(height = 3) 
       text(prenom, size = 11, font = str(font, style), $fn = 20);
}

module roundedBox(x,y,z,rad){
	hull() {
        translate([-x/2+rad, y/2-rad,-z/2]) cylinder(h=z,r=rad, $fn=50);
        translate([ x/2-rad, y/2-rad,-z/2]) cylinder(h=z,r=rad, $fn=50);
        translate([-x/2+rad,-y/2+rad,-z/2]) cylinder(h=z,r=rad, $fn=50);
        translate([ x/2-rad,-y/2+rad,-z/2]) cylinder(h=z,r=rad, $fn=50);
   }
}
