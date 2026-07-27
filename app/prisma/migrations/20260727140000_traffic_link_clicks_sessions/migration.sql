-- AlterTable
-- Traffic diagnostics: paid link clicks + store sessions (not path attribution)

CREATE TABLE "LinkClickEntry" (
    "id" TEXT NOT NULL,
    "shopId" TEXT NOT NULL,
    "channel" "SpendChannel" NOT NULL,
    "clicks" INTEGER NOT NULL,
    "periodStart" TIMESTAMP(3) NOT NULL,
    "periodEnd" TIMESTAMP(3) NOT NULL,
    "note" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "LinkClickEntry_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "SessionEntry" (
    "id" TEXT NOT NULL,
    "shopId" TEXT NOT NULL,
    "sessions" INTEGER NOT NULL,
    "periodStart" TIMESTAMP(3) NOT NULL,
    "periodEnd" TIMESTAMP(3) NOT NULL,
    "note" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "SessionEntry_pkey" PRIMARY KEY ("id")
);

CREATE INDEX "LinkClickEntry_shopId_periodStart_periodEnd_idx" ON "LinkClickEntry"("shopId", "periodStart", "periodEnd");

CREATE INDEX "SessionEntry_shopId_periodStart_periodEnd_idx" ON "SessionEntry"("shopId", "periodStart", "periodEnd");

ALTER TABLE "LinkClickEntry" ADD CONSTRAINT "LinkClickEntry_shopId_fkey" FOREIGN KEY ("shopId") REFERENCES "Shop"("id") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "SessionEntry" ADD CONSTRAINT "SessionEntry_shopId_fkey" FOREIGN KEY ("shopId") REFERENCES "Shop"("id") ON DELETE CASCADE ON UPDATE CASCADE;
