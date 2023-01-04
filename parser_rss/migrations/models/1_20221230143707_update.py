from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" ADD "summary" TEXT;
        ALTER TABLE "article" ADD "title" TEXT NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" DROP COLUMN "summary";
        ALTER TABLE "article" DROP COLUMN "title";"""
