import { faker } from '@faker-js/faker';
import { $ } from 'execa';

const prTypes = ['feat', 'chore', 'fix', 'docs', 'perf', 'test'];
const teams = ['search', 'ci', 'cody'];

const randomInt = (max: number) => Math.floor(Math.random() * max);

function randomChoice<T>(elems: T[]): T {
  return elems[randomInt(elems.length)];
}

interface PR {
  type: string;
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
    team: randomChoice(teams),
    title: faker.lorem.sentence({ max: 7, min: 3 }),
    body: {
      description: faker.lorem.paragraph(),
      changelog: Array(1 + randomInt(3))
        .fill(undefined)
        .map((_) => faker.lorem.words({ min: 5, max: 10 }))
    }
  };
}

const prTitle = (pr: PR) => `${pr.type}/${pr.team}: ${pr.title}`;

const prBody = (pr: PR) => `${pr.body.description}

Changelog:
${' - ' + pr.body.changelog.join('\n - ')}`;

async function main() {
  for (let i = 0; i < 1; i++) {
    const pr = generatePR();
    const { stdout } = await $`gh pr create --title '${prTitle(
      pr
    )} --body '${prBody(pr)}'`;
    console.log(stdout);
    // console.log(prBody(pr));
  }
}

main();
