// Bootstrap from https://www.bootstrapcdn.com/

function ageInDays(){
    let birthyear = prompt('What year were you born ? \n dd-mm-yyyy');
    var today = new Date();
    let birth = birthyear.split('-')
    // Year
    let days = Number(today.getFullYear() - birth[2]) * 365;
    // Month
    days -= Number(birth[1])*30
    days += today.getMonth()*30
    // Days
    days += today.getDate()
    days += Number(30-birth[0])
    var h1 = document.createElement('h1');
    var textanswer = document.createTextNode('You are '+ days +' days old.');
    h1.setAttribute('id', 'days');
    h1.appendChild(textanswer);
    document.getElementById('flex-box-result').appendChild(h1);
}  

function reset(){
    document.getElementById('days').remove();
}