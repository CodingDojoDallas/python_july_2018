function invertHash(obj){
    var newObj={};
    for(i in obj){
        newObj.obj[i]=i;
    }
    return newObj
}
console.log(invertHash({2:4,6:8,10:12}));