from pool.init_db import (
    DSN,
    create_engine,
    create_tables,
    setup_db,
    teardown_db,
)
from pool.api.settings import CONFIG
from pytest import fixture
import sqlalchemy as sa


@fixture(scope="module")
def test_dsn():
    dsn = DSN.format(**CONFIG["postgres"])
    assert dsn == "postgresql://postgres:password@localhost:5432/pool"
    return dsn


@fixture(scope="function")
def test_db(test_dsn):
    engine = create_engine(test_dsn)
    setup_db(CONFIG["postgres"])
    create_tables(engine)
    assert sa.inspect(engine).has_table("player")
    yield engine
    teardown_db(CONFIG["postgres"])
