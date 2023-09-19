interface Autenticacao {
    final int TAMANHO_SENHA = 12;
    void autentica(String login, String senha);
}