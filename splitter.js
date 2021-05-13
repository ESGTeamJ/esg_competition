// It splits string with specific repeating delimimter to an array of strings 
const splitter = (string) => {
    namesArr = string.split(""); //add here your delimiter in our case: /;*_/
    console.log(JSON.stringify(namesArr));
}
// input: "Hello/;*_/World" => output: ["Hello","World"]
