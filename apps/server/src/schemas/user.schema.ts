import { z } from "zod";

const signUp = z.object({
  name: z.string().min(3),
  email: z.email(),
  password: z.string().min(3).max(8),
});
export type signUpInput = z.infer<typeof signUp>;

const logIn = z.object({
  email: z.email(),
  password: z.string().min(3).max(8),
});
export type logInInput = z.infer<typeof logIn>;

const UserSchema = { signUp, logIn };

export default UserSchema;
