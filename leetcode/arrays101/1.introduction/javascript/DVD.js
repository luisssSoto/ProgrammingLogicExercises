"use strict";

class DVD {
    name = String();
    releaseYear = Number();
    director = String();

    constructor(name, releaseYear, director) {
        this.name = name;
        this.releaseYear = releaseYear;
        this.director = director;
    };

    getDetails() {
        return `${this.name} directed by ${this.director}, released in ${this.releaseYear} year.`
    };
};

let lordOfTheRings = new DVD('The Lord Of The Rings', 2001, 'Peter Jackson');
console.log(lordOfTheRings.getDetails());

//Creating an array
let dvdCollection = Array(6);
console.log(dvdCollection.length);

//Writing items inside an array
dvdCollection[1] = lordOfTheRings;

//Reading items from an array
console.log(dvdCollection[1]);
console.log(dvdCollection[1].getDetails());

//Capacity
console.log(`Capacity of dvd collection: ${dvdCollection.length}`);

//Length
let length = 0;
for (let dvd of dvdCollection) {
    if (!(typeof dvd === 'undefined')) {
        length ++;
    };
};
console.log(`Length of dvd collection: ${length}`)