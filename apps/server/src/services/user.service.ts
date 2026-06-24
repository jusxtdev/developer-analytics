 import { prisma } from "@/config/db.js";
import { Prisma } from "@/generated/prisma/client.js";
import { AppError } from "@/utils/appError.js";

const findUserByEmail = async (email: string) => {
  try {
    const user = await prisma.user.findUniqueOrThrow({
      where: {
        email: email,
      },
      select : {
        id : true,
        name : true,
        email : true,
        password : true,
        createdAt : true
      }
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

const signupUser = async (name: string, email: string, hashedPass: string) => {
  try {
    const newuser = await prisma.user.create({
      data: {
        name: name,
        email: email,
        password: hashedPass,
      },
      select : {
        id : true,
        name : true,
        email : true,
        createdAt : true
      }
    });
    return newuser;
  } catch (e) {
    if (e instanceof Prisma.PrismaClientKnownRequestError){
      if (e.code === "P2002"){
        // user already exists
        throw new AppError("User already exists", 409, false)
      }
    }
    console.error(e);
    throw AppError.internal()
  }
};


const UserService = { findUserByEmail, signupUser };
export default UserService;
