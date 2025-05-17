class MyArray {
    constructor(size) {
        this.array = Array(size);
    };
    getArray() {
        return this.array;
    };
    readElement(index) {
        if (index > this.array.length - 1) {
            return `Sorry but the element which you are looking: ${this.array[index]} doesn't exist`;
        } else {
            return this.array[index];
        };
    };
    insertElement(element, index) {
        if (index >= this.array.length) {
            return `Sorry but the element which you are looking for at the index: ${index} to insert is out of the range of the array: ${this.array.length}`;
        } else {
            this.array[index] = element;
            return `Successfull insertion`;
        };
    };
    deleteElement(index) {
        if (index >= this.array.length) {
            return `Sorry but the element which you are looking for at the index: ${index} to delete is out of the range of the array: ${this.array.length}`;
        } else if (index == this.array.length - 1) {
            this.array[index] = undefined;
        } else {
            for (let i = index; i < this.array.length - 1; i++) {
                this.array[i] = this.array[i + i];
            };
            return `Successfull deletion`;
        };
        
    };
};

let myArray1 = new MyArray(6);
console.log(myArray1);
console.log(myArray1.getArray());
console.log(myArray1.readElement(6));
console.log(myArray1.readElement(5));
console.log(myArray1.insertElement(10, 4));
console.log(myArray1.getArray());
console.log(myArray1.deleteElement(4));
console.log(myArray1.getArray());
