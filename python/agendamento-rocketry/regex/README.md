# Usando expressão regular

Uso de algumas expressões regulares.

Fonte: https://www.youtube.com/watch?v=tlVI8mV1dQY

Site:

- regexr.com
- jsfiddle.net

## Expressões

```
este é um tExto qualquer

/e/gi: pega todos os "e", case insensitive
```

```
let text = 'este é um texto';
let regex = /texto/g;

<!--string para testar uma expreão-->
let resultado1 = text.match(regex);

console.log(resultado1);

<!--expressão para testar uma string-->
let resultado2 = regex.exec(text);

console.log(resultado2);

<!--testando se encontrou ocorrências-->
let resultado3 = regex.test(text);

console.log(resultado3);
```

```
/./gi: acha qualquer caracter

/t./gi: acha um t e qualquer coisa

/e|é/gi: pega o e ou o é

/(tex)|(q)/gi: dois grupos, acha tex ou q

/[eéq]/gi: pega todos as ocorrências de e, é e q


/[a-e]/gi: pega a sequencia a, e, i, o, u

/[a-z]/gi: pega todos dentro do intervalo

/[^et]: pega todos meno o e e o t

/[(a-z)(A-Z)]/g: pega de a a z caixa alta e baixa

/(e+)/g: pega um ou mais letras e, em sequencia

/(e+)?/g: pega tudo, pois esta opicional

/e{2,3}/g:repetições com qtd exatas, pega quando tem 2 ou 3 e juntos.


/^este/g: pega apenas se começar com este.

/o$/: pega se termina em o (se tiver final de linha, não pega)


```
