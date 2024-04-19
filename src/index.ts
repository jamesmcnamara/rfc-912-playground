import { faker } from '@faker-js/faker';
import { $, ExecaChildProcess, ExecaReturnValue, execa } from 'execa';

const $$ = $({ stdio: 'inherit' });
const prTypes = ['feat', 'chore', 'fix', 'docs', 'perf', 'test'];
const teams = ['search', 'ci', 'cody'];

const randomInt = (max: number) => Math.floor(Math.random() * max);

function randomChoice<T>(elems: T[]): T {
  return elems[randomInt(elems.length)];
}

const range = (n: number) => Array.from(Array(n).keys());

const hackerPhrase = ({
  sentences = 1
}: {
  sentences?: number;
} = {}): string =>
  range(sentences)
    .map((_) => faker.hacker.phrase())
    .join(' ')
    .replace(/!/g, '.');

interface PR {
  type: string;
  branch: string;
  team: string;
  title: string;
  body: Body;
}

interface Body {
  description: string;
  changelog: string[];
}

function generatePR(): PR {
  return {
    type: randomChoice(prTypes),
    branch: `${faker.string
      .alpha({ length: 3 })
      .toLowerCase()}/${faker.git.branch()}`,
    team: randomChoice(teams),
    title: hackerPhrase(),
    body: {
      description: hackerPhrase({ sentences: 3 }),
      changelog: range(1 + randomInt(3)).map(() => hackerPhrase())
    }
  };
}

const prTitle = (pr: PR) => `${pr.type}/${pr.team}: ${pr.title}`;

const prBody = (pr: PR) => `${pr.body.description}

Changelog:
${' - ' + pr.body.changelog.join('\n - ')}`;

async function main() {
  for (let i = 0; i < 10; i++) {
    const pr = generatePR();
    await $$`git checkout -b ${pr.branch}`;

    await $`echo '${faker.lorem.words({
      min: 5,
      max: 10
    })}'`.pipeStdout?.(`dummies/${faker.lorem.slug({ min: 3, max: 5 })}.txt`);
    await $$`git add dummies/*`;
    await $$`git commit -m ${prTitle(pr)}`;
    await $$`git push origin ${pr.branch}`;

    const { stdout: url } = await $`gh pr create --base main --title ${prTitle(
      pr
    )} --body ${prBody(pr)}`;

    await $$`gh pr merge --squash ${url}`;
  }
}

main();
