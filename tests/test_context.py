from src.context.context_builder import ContextBuilder

CLIENTE_EXISTENTE = 1
CLIENTE_INEXISTENTE = 9999


def test_load_profile_cliente_existente():
    builder = ContextBuilder()
    perfil = builder.load_profile(CLIENTE_EXISTENTE)

    assert perfil != {}
    assert perfil["cliente_id"] == CLIENTE_EXISTENTE
    assert "perfil" in perfil


def test_load_profile_cliente_inexistente():
    builder = ContextBuilder()
    perfil = builder.load_profile(CLIENTE_INEXISTENTE)

    assert perfil == {}


def test_load_portfolio():
    builder = ContextBuilder()
    carteira = builder.load_portfolio(CLIENTE_EXISTENTE)

    assert isinstance(carteira, list)
    assert len(carteira) > 0
    assert "produto" in carteira[0]


def test_load_transactions():
    builder = ContextBuilder()
    transacoes = builder.load_transactions(CLIENTE_EXISTENTE)

    assert isinstance(transacoes, list)
    assert len(transacoes) > 0


def test_load_products():
    builder = ContextBuilder()
    produtos = builder.load_products()

    assert isinstance(produtos, list)
    assert len(produtos) > 0
    assert "perfil_recomendado" in produtos[0]


def test_load_history_arquivo_existente():
    builder = ContextBuilder()
    historico = builder.load_history(CLIENTE_EXISTENTE)

    assert isinstance(historico, list)


def test_build_context_possui_todas_as_chaves():
    builder = ContextBuilder()
    contexto = builder.build_context(CLIENTE_EXISTENTE)

    for chave in ["perfil", "carteira", "transacoes", "historico", "produtos"]:
        assert chave in contexto