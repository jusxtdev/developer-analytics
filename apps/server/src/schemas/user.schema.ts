import { z } from "zod";

const createUser = z.object({
  name: z.string().min(3),
  email: z.email(),
  password: z.string().min(3).max(8),
});
export type createUserInput = z.infer<typeof createUser>;

const UserSchema = { createUser };

export default UserSchema;
