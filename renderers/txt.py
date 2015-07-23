class Renderer(object):
    def __init__(self, runtime):
        self.runtime = runtime

    def render(self):
        with open('triage.txt', 'w') as f:
            f.write('''PUPPET MODULE TRIAGE


Open Questions
==============




Repositories
============

''')
            runtime = self.runtime
            for repository in runtime.repositories.values():
                repo = repository
                f.write('%s\n%s\n' % (repository.name, str('{:-^%s}' % str(len(repository.name))).format('-')))

                if not repository.internal:
                    f.write('Repository has no internal remote\n')
                    continue

                if not repository.upstream:
                    f.write('Repository has no upstream remote\n')
                else:
                    if repo.behind == 0:
                        f.write('Repository is not behind upstream - good.\n\n')
                    else:
                        f.write('Repository is %s commits behind upstream!\n\n' % repo.behind)
                    if repo.ahead == 0:
                        f.write('Repository is not ahead upstream - good.\n\n')
                    else:
                        f.write('Repository is %s commits ahead upstream!\n\n' % repo.ahead)
                    if len(repo.internal.tickets) > 0:
                        f.write('Internal tickets:\n\n')
                        for ticket in repo.internal.tickets:
                            f.write(' * %s%s - %s - %s\n   %s\n' % (repository.internal.ticket_prefix, ticket.reference, ticket.external.status[1], ticket.external.title, ticket.url))
                        f.write('\n\n')
                    if len(repo.upstream.tickets) > 0:
                        f.write('Upstream tickets:\n\n')
                        for ticket in repo.upstream.tickets:
                            f.write(' * %s%s - %s - %s\n   %s\n' % (repository.upstream.ticket_prefix, ticket.reference, ticket.external.status[1], ticket.external.title))
                        f.write('\n\n')
                    if repo.behind > 0:
                        f.write('Repo is behind upstream.\n\n')
                        f.write('Is there already a ticket for that? yes-no\n')
                        f.write('Ticket number:\n')
                        f.write('Do the upstream changes look trivial? yes-no\n')
                        f.write('Comments:\n')
                        f.write('\n')
                        f.write('\n')
                    if repo.ahead > 0:
                        f.write('Repository is ahead upstream.\n\n')
                        f.write('Is there already a ticket for that? yes-no\n')
                        f.write('Ticket number:\n')
                        f.write('Do the internal changes look trivial? yes-no\n')
                        f.write('Do the local commits include Inuits specific code? yes-no\n')
                        f.write('Does the local code have good quality? yes-no\n')
                        f.write('Comments:\n')
                        f.write('\n')
                        f.write('\n')

                    for diff in repo.diffs.values():
                        if diff.behind is not None:
                            if diff.behind == 0:
                                f.write('Repository is not behind in super repo %s - good.\n\n' % diff.target)
                            else:
                                f.write('Repository is %s commits behind in super repo %s!\n\n' % (diff.behind, diff.target))
                                f.write('Is there already a ticket for that?\n')
                                f.write('Ticket number:\n')
                                f.write('Comments:\n\n\n')
                            if diff.ahead == 0:
                                f.write('Repository is not ahead in super repo %s - good.\n\n' % diff.target)
                            else:
                                f.write('Repository is %s commits ahead in super repo %s!\n\n' % (diff.ahead, diff.target))
                                f.write('Is there already a ticket for that?\n')
                                f.write('Ticket number:\n')
                                f.write('Comments:\n\n\n')


                f.write('\n')
                f.write('\n')