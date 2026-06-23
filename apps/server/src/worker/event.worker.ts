import { Worker, Job } from 'bullmq';
import { redisConnection } from '../config/redis.js';
import { eventInput } from '@/schemas/eventBatch.schema.js';
import RawEventService from '@/services/rawEvent.service.js';


export const eventWorker = new Worker(
  'batch-queue',
  async (job :Job<eventInput>) => {
    const event = job.data;
    console.log('Processing:', event);

    await RawEventService.addEvent(event)
  },
  {
    connection: redisConnection,
    concurrency: 5,                  // process 5 jobs in parallel
  }
);

eventWorker.on('completed', (job:Job<eventInput>) => {
  console.log(`Job ${job.id} finished`);
});

eventWorker.on('failed', (job :Job<eventInput> | undefined, err:Error) => {
  console.error(`Job ${job?.id} failed:`, err.message);
});