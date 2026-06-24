import { createUserInput } from "@/schemas/user.schema.js";
import UserService from "@/services/user.service.js";
import { ApiResponse } from "@/utils/apiResponse.js";
import generateToken, { jwtPayload } from "@/utils/generateToken.js";
import storeCookie from "@/utils/storeCookie.js";
import bcrypt from "bcrypt";
import { Request, Response } from "express";

const signup = async (req: Request, res: Response) => {
  const body: createUserInput = req.body;

  const SALT = await bcrypt.genSalt(10);
  const hashedPass = await bcrypt.hash(body.password, SALT);

  const newUser = await UserService.createUser(body.name, body.email, hashedPass)
  
  const payload : jwtPayload = {
    userId : newUser.id,
    email : newUser.email
  } 
  const token = generateToken(payload)

  storeCookie("jwt", token, res)

  return ApiResponse.created(res, "Signup Successfull", )
};

const AuthController = { signup };

export default AuthController;
