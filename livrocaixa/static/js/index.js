$('.form').find('input, textarea').on('keyup blur focus', function (e) {

    var $this = $(this),
            label = $this.prev('label');

    if (e.type === 'keyup') {
        if ($this.val() === '') {
            label.removeClass('active highlight');
        } else {
            label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
        if ($this.val() === '') {
            label.removeClass('active highlight');
        } else {
            label.removeClass('highlight');
        }
    } else if (e.type === 'focus') {

        if ($this.val() === '') {
            label.removeClass('highlight');
        } else if ($this.val() !== '') {
            label.addClass('highlight');
        }
    }

});

function ajuda() {
    alert("- Para adicionar uma nova receita clique no botão logo abaixo de 'Adicionar Receita'.\n\
\n \n- Para procurar por uma receita já existente clique na aba 'Minhas Receitas'.\n\
\n \n- Para acessar as receitas públicas clique no botão logo abaixo 'Receitas Publicas'.\n\ ");
}



$('.tab a').on('click', function (e) {

    e.preventDefault();

    $(this).parent().addClass('active');
    $(this).parent().siblings().removeClass('active');

    target = $(this).attr('href');

    $('.tab-content > div').not(target).hide();

    $(target).fadeIn(600);

});
