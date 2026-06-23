import { z } from "zod";

const event = z.object({
  timestamp: z.string().transform((val) => new Date(val)),
  title: z.string(),
  application: z.string(),
  isIdle: z.boolean(),
});
export type eventInput = z.infer<typeof event>;

const batch = z.array(event);
export type batchInput = z.infer<typeof batch>;

const batchSchema = { batch, event };

export default batchSchema;
