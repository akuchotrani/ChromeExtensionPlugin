console.log("Hello from word joy content.js");

let paragraphs = document.getElementsByTagName('p');
let textContent = " ";

for(elt of paragraphs)
{
    textContent += elt.textContent + " "
}

console.log(textContent);
