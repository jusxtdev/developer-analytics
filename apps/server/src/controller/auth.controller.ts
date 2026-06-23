import { createUserInput } from "@/schemas/user.schema.js";
import UserService from "@/services/user.service.js";
import bcrypt from "bcrypt";
import { Request, Response } from "express";

const signup = async (req: Request, res: Response) => {
  const body: createUserInput = req.body;

  const user = await UserService.userExists(body.email);
  if (user) {
    return res.status(409).json({
      msg: "User Already exists",
    });
  }
  const SALT = await bcrypt.genSalt(10);
  const hashedPass = await bcrypt.hash(body.password, SALT);

  const newUser = await UserService.createUser(body.name, body.email, hashedPass)
  res.status(200).json({
    msg:"Signup Successful",
    data : newUser
  })
};

const AuthController = { signup };

export default AuthController;
