function valida_novo_usuario(tipo_de_verificacao) {
    if(tipo_de_verificacao == "apelido"){
        var id = "#apelido_register"
        var valor_do_input = $(id).val();
        var re = /^([a-z0-9]){4,}$/
    } else if(tipo_de_verificacao == "senha"){
        var id = "#senha_register"
        var valor_do_input = $(id).val();
        var re = /^(.){6,}$/
    }
    
    if(re.exec(valor_do_input) == null){
        $(id).removeClass("is-valid");
        $(id).addClass("is-invalid");
    }
    else {
        $(id).removeClass("is-invalid");
        $(id).addClass("is-valid");
    }
}
