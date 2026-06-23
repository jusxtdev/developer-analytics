-- CreateTable
CREATE TABLE "APIKeys" (
    "id" SERIAL NOT NULL,
    "userId" INTEGER NOT NULL,
    "kayHash" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "APIKeys_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "RawEvents" (
    "id" SERIAL NOT NULL,
    "timestamp" TIMESTAMP(3) NOT NULL,
    "window_title" TEXT NOT NULL,
    "application" TEXT NOT NULL,
    "isIdle" BOOLEAN NOT NULL,
    "userId" INTEGER NOT NULL,

    CONSTRAINT "RawEvents_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "APIKeys" ADD CONSTRAINT "APIKeys_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "RawEvents" ADD CONSTRAINT "RawEvents_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
