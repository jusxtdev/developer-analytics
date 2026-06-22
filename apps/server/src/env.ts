import { createEnv } from "@t3-oss/env-core";
import { z } from "zod";
import { config } from "dotenv";
config();

/**
 * Used to access environment variables
 * from JS Object
 */
export const env = createEnv({
  server: {
    PORT: z.coerce.number(),
    DATABASE_URL: z.url(),
    NODE_ENV: z.string(),
  },
  runtimeEnv: process.env,
});