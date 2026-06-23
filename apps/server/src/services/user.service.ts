import { prisma } from "@/config/db.js";
import { Prisma } from "@/generated/prisma/client.js";

const userExists = async (email: string) => {
  try {
    const user = await prisma.user.findUniqueOrThrow({
      where: {
        email: email,
      },
    });
    return user;
  } catch (error) {
    if (error instanceof Prisma.PrismaClientKnownRequestError) {
      // Record not found
      if (error.code === "P2025") {
        return null;
      }
    }
    console.error(error);
  }
};

const createUser = async (name: string, email: string, hashedPass: string) => {
  try {
    const newuser = await prisma.user.create({
      data: {
        name: name,
        email: email,
        password: hashedPass,
      },
    });
    return newuser;
  } catch (e) {
    console.error(e);
    return null;
  }
};

const UserService = { userExists, createUser };
export default UserService;
