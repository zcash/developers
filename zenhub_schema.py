import sgqlc.types
import sgqlc.types.relay


zenhub_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
zenhub_schema -= sgqlc.types.relay.Node
zenhub_schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class BigInt(sgqlc.types.Scalar):
    __schema__ = zenhub_schema


Boolean = sgqlc.types.Boolean

class BucketIssueHistoryAction(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('ISSUE_ADDED', 'ISSUE_REMOVED')


class DisplayFilter(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('all', 'issues', 'prs')


class EpicOrderField(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CREATED_AT', 'TITLE')


class EpicSpecialFilter(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('epics_only', 'epics_with_subtasks', 'no_epics', 'not_in_epic')


class EstimateSpecialFilter(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('assigned_for_voting', 'assigned_to_user_for_voting', 'not_estimated')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

class ISO8601Date(sgqlc.types.Scalar):
    __schema__ = zenhub_schema


class ISO8601DateTime(sgqlc.types.Scalar):
    __schema__ = zenhub_schema


Int = sgqlc.types.Int

class IssueDependencyItemState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'OPEN')


class IssueOrderField(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('assignees', 'created_at', 'estimate', 'sprints', 'stale', 'title', 'updated_at')


class IssueState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'OPEN')


class IssueType(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('GithubIssue', 'ZenhubIssue')


class JSON(sgqlc.types.Scalar):
    __schema__ = zenhub_schema


class MatchingFilter(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('all', 'any')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('ASC', 'DESC')


class PermissionLevel(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('ADMIN', 'NONE', 'READ', 'WRITE', 'ZENHUB_WRITE')


class PipelineIssuePosition(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('END', 'START')


class PipelineStage(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('BACKLOG', 'COMPLETED', 'DEVELOPMENT', 'REVIEW', 'SPRINT_BACKLOG')


class ProjectDateAction(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('RESET', 'SCALE', 'SHIFT')


class ProjectState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'OPEN')


class PullRequestReviewState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('APPROVED', 'CHANGES_REQUESTED', 'COMMENTED', 'DISMISSED')


class PullRequestState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'MERGED', 'OPEN')


class ReleaseState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'OPEN')


class RepositoryImportResourceKind(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED_ISSUES', 'OPEN_ISSUES')


class RepositoryImportResourceState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('COMPLETED', 'IN_PROGRESS', 'PENDING')


class RepositoryImportState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('COMPLETED', 'IN_PROGRESS', 'PENDING', 'USABLE')


class RepositoryType(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('GithubRepository', 'ZenhubRepository')


class RoadmapItemOrderField(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('end_on', 'start_on')


class RoadmapItemState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'IN_PROGRESS', 'OPEN', 'TODO')


class Roles(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('ADMIN', 'EXTERNAL_READER', 'EXTERNAL_WRITER', 'MEMBER')


class SprintConfigDayOfTheWeek(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY')


class SprintConfigKind(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('monthly', 'weekly')


class SprintOrderField(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('END_AT', 'START_AT')


class SprintReviewState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('COMPLETED', 'INITIAL', 'IN_PROGRESS')


class SprintSpecialFilter(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('current_sprint',)


class SprintState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'OPEN')


String = sgqlc.types.String

class WorkspaceImportState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('COMPLETED', 'IN_PROGRESS', 'PENDING', 'USABLE')


class ZenhubEpicOrderField(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('ASSIGNEES', 'CREATED_AT', 'END_ON', 'START_ON', 'STATE', 'TITLE', 'UPDATED_AT')


class ZenhubEpicSpecialFilter(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('not_in_epic',)


class ZenhubEpicState(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('CLOSED', 'IN_PROGRESS', 'OPEN', 'TODO')


class ZenhubUserOrderField(sgqlc.types.Enum):
    __schema__ = zenhub_schema
    __choices__ = ('DISPLAY_NAME',)



########################################################################
# Input Objects
########################################################################
class AcceptZenhubOrganizationInviteInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'token')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')


class AddAssigneesToIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'assignee_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')


class AddAssigneesToZenhubEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'assignee_ids', 'zenhub_epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')


class AddEpicsToProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='epicIds')


class AddEpicsToRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic_ids', 'roadmap_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='epicIds')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')


class AddEstimateSetValueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class AddIssuesToEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='epicIds')


class AddIssuesToReleasesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'release_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    release_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='releaseIds')


class AddIssuesToSprintsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'sprint_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    sprint_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='sprintIds')


class AddIssuesToZenhubEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'zenhub_epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')


class AddLabelsToIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'label_ids', 'label_infos')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    label_infos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LabelInfoInput')), graphql_name='labelInfos')


class AddMilestoneForIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'milestone_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    milestone_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='milestoneId')


class AddProjectsToRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'project_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    project_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='projectIds')


class AddRepositoriesToReleaseInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'repository_gh_ids', 'release_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_gh_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='repositoryGhIds')
    release_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='releaseId')


class AddRepositoryToWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'repository_gh_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    repository_gh_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryGhId')


class AddWorkspaceLabelFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'label_names')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    label_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='labelNames')


class AddZenhubAssigneesToIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'zenhub_user_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    zenhub_user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubUserIds')


class AddZenhubEpicsToProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'zenhub_epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')


class AddZenhubEpicsToRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'zenhub_epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')


class AddZenhubLabelsToIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'zenhub_label_ids', 'label_infos')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    zenhub_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='zenhubLabelIds')
    label_infos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LabelInfoInput')), graphql_name='labelInfos')


class AddZenhubLabelsToZenhubEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_ids', 'zenhub_label_ids', 'label_infos')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')
    zenhub_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='zenhubLabelIds')
    label_infos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LabelInfoInput')), graphql_name='labelInfos')


class AddZenhubRepositoryToWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class AddZenhubUsersToWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_user_ids', 'workspace_id', 'workspace_user_roles')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubUserIds')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    workspace_user_roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceRoleInput')), graphql_name='workspaceUserRoles')


class CloseIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')


class ConvertZenhubIssueToGithubIssueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class CreateCommentInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'commentable_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    commentable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='commentableId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class CreateEpicFromIssueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'epic_child_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    epic_child_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='epicChildIds')


class CreateEpicInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('IssueInput'), graphql_name='issue')


class CreateEpicOnProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('EpicInput'), graphql_name='epic')


class CreateEpicOnRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('EpicInput'), graphql_name='epic')


class CreateGithubLabelInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name', 'color', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')


class CreateIssueDependencyInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'blocking_issue', 'blocked_issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    blocking_issue = sgqlc.types.Field(sgqlc.types.non_null('IssueInfoInput'), graphql_name='blockingIssue')
    blocked_issue = sgqlc.types.Field(sgqlc.types.non_null('IssueInfoInput'), graphql_name='blockedIssue')


class CreateIssueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'title', 'body', 'labels', 'assignees')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels')
    assignees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='assignees')


class CreateIssuePrConnectionInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'pull_request_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')


class CreateMilestoneInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'title', 'description', 'due_on', 'start_date')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    due_on = sgqlc.types.Field(ISO8601DateTime, graphql_name='dueOn')
    start_date = sgqlc.types.Field(ISO8601DateTime, graphql_name='startDate')


class CreatePipelineAutomationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_id', 'element_details')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')
    element_details = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='elementDetails')


class CreatePipelineInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'name', 'position', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    position = sgqlc.types.Field(Int, graphql_name='position')
    description = sgqlc.types.Field(String, graphql_name='description')


class CreatePipelineToPipelineAutomationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'source_pipeline_id', 'destination_pipeline_id', 'apply_retroactively')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    source_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sourcePipelineId')
    destination_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='destinationPipelineId')
    apply_retroactively = sgqlc.types.Field(Boolean, graphql_name='applyRetroactively')


class CreateProjectOnRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    project = sgqlc.types.Field(sgqlc.types.non_null('ProjectInput'), graphql_name='project')


class CreateReleaseInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'release')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    release = sgqlc.types.Field(sgqlc.types.non_null('ReleaseCreateInput'), graphql_name='release')


class CreateRoadmapKeyDateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'date', 'description', 'color')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    date = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='date')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    color = sgqlc.types.Field(String, graphql_name='color')


class CreateSavedViewInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'name', 'filters')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    filters = sgqlc.types.Field(sgqlc.types.non_null('IssueSearchFiltersInput'), graphql_name='filters')


class CreateSprintConfigInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_config')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_config = sgqlc.types.Field(sgqlc.types.non_null('SprintConfigCreateInput'), graphql_name='sprintConfig')


class CreateWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'name', 'description', 'zenhub_organization_id', 'repository_gh_ids', 'default_repository_gh_id', 'github_project', 'private', 'are_uploaded_files_private')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    zenhub_organization_id = sgqlc.types.Field(ID, graphql_name='zenhubOrganizationId')
    repository_gh_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='repositoryGhIds')
    default_repository_gh_id = sgqlc.types.Field(Int, graphql_name='defaultRepositoryGhId')
    github_project = sgqlc.types.Field('GithubProjectInput', graphql_name='githubProject')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    are_uploaded_files_private = sgqlc.types.Field(Boolean, graphql_name='areUploadedFilesPrivate')


class CreateZenhubEpicInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_id', 'zenhub_epic', 'zenhub_repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpicInput'), graphql_name='zenhubEpic')
    zenhub_repository_id = sgqlc.types.Field(ID, graphql_name='zenhubRepositoryId')


class CreateZenhubEpicKeyDateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_id', 'date', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')
    date = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='date')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class CreateZenhubEpicOnProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'zenhub_epic', 'zenhub_repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpicInput'), graphql_name='zenhubEpic')
    zenhub_repository_id = sgqlc.types.Field(ID, graphql_name='zenhubRepositoryId')


class CreateZenhubEpicOnRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpicInput'), graphql_name='zenhubEpic')


class CreateZenhubLabelInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_id', 'name', 'color', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')


class CreateZenhubOrganizationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateZenhubOrganizationInviteInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_id', 'expire_in_days', 'email_properties', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId')
    expire_in_days = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='expireInDays')
    email_properties = sgqlc.types.Field('EmailPropertiesInput', graphql_name='emailProperties')
    workspace_id = sgqlc.types.Field(ID, graphql_name='workspaceId')


class DeleteCommentInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'comment_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='commentId')


class DeleteEpicByIssueInfoInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('IssueInfoInput'), graphql_name='issue')


class DeleteIssueDependencyInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'blocking_issue', 'blocked_issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    blocking_issue = sgqlc.types.Field(sgqlc.types.non_null('IssueInfoInput'), graphql_name='blockingIssue')
    blocked_issue = sgqlc.types.Field(sgqlc.types.non_null('IssueInfoInput'), graphql_name='blockedIssue')


class DeleteIssuePrConnectionInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'pull_request_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')


class DeleteNotionIntegrationTokenInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeletePipelineAutomationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_automation_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_automation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineAutomationId')


class DeletePipelineInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_id', 'destination_pipeline_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')
    destination_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='destinationPipelineId')


class DeletePipelineToPipelineAutomationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_to_pipeline_automation_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_to_pipeline_automation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineToPipelineAutomationId')


class DeleteProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class DeleteRoadmapKeyDateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='keyDateId')


class DeleteSavedViewInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'saved_view_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    saved_view_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='savedViewId')


class DeleteSprintConfigAndOpenSprintsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class DeleteWorkspaceFavoriteInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class DeleteWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class DeleteZenhubEpicInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')


class DeleteZenhubEpicKeyDateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='keyDateId')


class DeleteZenhubIssueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class DeleteZenhubOrganizationInviteRecipientsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_invite_recipient_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_invite_recipient_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubOrganizationInviteRecipientIds')


class DeleteZenhubOrganizationInvitesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_invite_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_invite_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubOrganizationInviteIds')


class DeleteZenhubUserInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'auto_assign_admin')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    auto_assign_admin = sgqlc.types.Field(Boolean, graphql_name='autoAssignAdmin')


class DisconnectGithubUserInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DisconnectWorkspaceRepositoryInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'repository_gh_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    repository_gh_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repositoryGhId')


class DismissConnectNotionPromptInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DuplicatePipelineAutomationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_automation_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_automation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineAutomationId')


class EmailPropertiesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('recipients',)
    recipients = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='recipients')


class EpicAssignableIssueSearchFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('repository_ids', 'pipeline_ids')
    repository_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='repositoryIds')
    pipeline_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='pipelineIds')


class EpicInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('issue',)
    issue = sgqlc.types.Field(sgqlc.types.non_null('IssueInput'), graphql_name='issue')


class EpicOrderInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('direction', 'field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')
    field = sgqlc.types.Field(EpicOrderField, graphql_name='field')


class EpicSearchFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'special_filters')
    id = sgqlc.types.Field('IdInput', graphql_name='id')
    special_filters = sgqlc.types.Field(EpicSpecialFilter, graphql_name='specialFilters')


class EstimateSearchFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('values', 'special_filters')
    values = sgqlc.types.Field('FloatInput', graphql_name='values')
    special_filters = sgqlc.types.Field(EstimateSpecialFilter, graphql_name='specialFilters')


class FloatInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('not_in_any', 'in_', 'nin')
    not_in_any = sgqlc.types.Field(Boolean, graphql_name='notInAny')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='nin')


class GenerateSprintReviewInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_id', 'call_async')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sprintId')
    call_async = sgqlc.types.Field(Boolean, graphql_name='callAsync')


class GithubProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('github_project_id', 'github_project_repo_gh_id')
    github_project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='githubProjectId')
    github_project_repo_gh_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='githubProjectRepoGhId')


class IdInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('not_in_any', 'in_', 'nin')
    not_in_any = sgqlc.types.Field(Boolean, graphql_name='notInAny')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nin')


class InviteToEstimateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'zenhub_user_ids', 'workspace_id', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    zenhub_user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubUserIds')
    workspace_id = sgqlc.types.Field(ID, graphql_name='workspaceId')
    message = sgqlc.types.Field(String, graphql_name='message')


class IssueBucketIdsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')


class IssueDependencyItemFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('state',)
    state = sgqlc.types.Field('IssueDependencyItemStateInput', graphql_name='state')


class IssueDependencyItemStateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('eq',)
    eq = sgqlc.types.Field(sgqlc.types.non_null(IssueDependencyItemState), graphql_name='eq')


class IssueFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('repository_id', 'state')
    repository_id = sgqlc.types.Field(IdInput, graphql_name='repositoryId')
    state = sgqlc.types.Field('IssueStateInput', graphql_name='state')


class IssueInfoInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('repository_gh_id', 'repository_id', 'issue_number')
    repository_gh_id = sgqlc.types.Field(Int, graphql_name='repositoryGhId')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    issue_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issueNumber')


class IssueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('repository_id', 'repository_gh_id', 'title', 'body', 'labels', 'assignees')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    repository_gh_id = sgqlc.types.Field(Int, graphql_name='repositoryGhId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels')
    assignees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='assignees')


class IssueOrderInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(IssueOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class IssueSearchFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('repository_ids', 'match_type', 'display_type', 'labels', 'assignees', 'assignee_ids', 'users', 'user_ids', 'sprints', 'releases', 'estimates', 'zenhub_epics', 'issue_buckets')
    repository_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds')
    match_type = sgqlc.types.Field(MatchingFilter, graphql_name='matchType')
    display_type = sgqlc.types.Field(DisplayFilter, graphql_name='displayType')
    labels = sgqlc.types.Field('StringInput', graphql_name='labels')
    assignees = sgqlc.types.Field('IssueUserLoginInput', graphql_name='assignees')
    assignee_ids = sgqlc.types.Field('IssueUserIdInput', graphql_name='assigneeIds')
    users = sgqlc.types.Field('IssueUserLoginInput', graphql_name='users')
    user_ids = sgqlc.types.Field('IssueUserIdInput', graphql_name='userIds')
    sprints = sgqlc.types.Field('SprintIdInput', graphql_name='sprints')
    releases = sgqlc.types.Field(IdInput, graphql_name='releases')
    estimates = sgqlc.types.Field(EstimateSearchFiltersInput, graphql_name='estimates')
    zenhub_epics = sgqlc.types.Field('ZenhubEpicSearchFiltersInput', graphql_name='zenhubEpics')
    issue_buckets = sgqlc.types.Field(IssueBucketIdsInput, graphql_name='issueBuckets')


class IssueStateFilterInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('in_', 'nin')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='nin')


class IssueStateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('eq',)
    eq = sgqlc.types.Field(sgqlc.types.non_null(IssueState), graphql_name='eq')


class IssueUserIdInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('not_in_any', 'in_', 'nin')
    not_in_any = sgqlc.types.Field(Boolean, graphql_name='notInAny')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nin')


class IssueUserLoginInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('not_in_any', 'in_', 'nin')
    not_in_any = sgqlc.types.Field(Boolean, graphql_name='notInAny')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')


class LabelInfoInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('name', 'color')
    name = sgqlc.types.Field(String, graphql_name='name')
    color = sgqlc.types.Field(String, graphql_name='color')


class LeaveZenhubOrganizationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_id', 'auto_assign_admin')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId')
    auto_assign_admin = sgqlc.types.Field(Boolean, graphql_name='autoAssignAdmin')


class MoveAllPipelineIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_ids', 'destination_pipeline_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='pipelineIds')
    destination_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='destinationPipelineId')


class MoveIssueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_id', 'issue_id', 'position')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    position = sgqlc.types.Field(Int, graphql_name='position')


class MoveIssueRelativeToInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'position', 'pipeline_id', 'after_pipeline_issue_id', 'before_pipeline_issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    position = sgqlc.types.Field(PipelineIssuePosition, graphql_name='position')
    pipeline_id = sgqlc.types.Field(ID, graphql_name='pipelineId')
    after_pipeline_issue_id = sgqlc.types.Field(ID, graphql_name='afterPipelineIssueId')
    before_pipeline_issue_id = sgqlc.types.Field(ID, graphql_name='beforePipelineIssueId')


class MovePipelineIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_id', 'pipeline_issue_ids', 'position', 'after_pipeline_issue_id', 'before_pipeline_issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')
    pipeline_issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='pipelineIssueIds')
    position = sgqlc.types.Field(PipelineIssuePosition, graphql_name='position')
    after_pipeline_issue_id = sgqlc.types.Field(ID, graphql_name='afterPipelineIssueId')
    before_pipeline_issue_id = sgqlc.types.Field(ID, graphql_name='beforePipelineIssueId')


class MoveRoadmapItemRelativeToInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'item_id', 'after_item_id', 'before_item_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')
    after_item_id = sgqlc.types.Field(ID, graphql_name='afterItemId')
    before_item_id = sgqlc.types.Field(ID, graphql_name='beforeItemId')


class MoveZenhubIssueToWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class ProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class ReleaseCreateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('title', 'description', 'start_on', 'end_on', 'repository_gh_ids')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    start_on = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='startOn')
    end_on = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='endOn')
    repository_gh_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='repositoryGhIds')


class ReleaseStateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('eq',)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ReleaseState), graphql_name='eq')


class ReleaseUpdateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('title', 'description', 'state', 'start_on', 'end_on')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    state = sgqlc.types.Field(ReleaseState, graphql_name='state')
    start_on = sgqlc.types.Field(ISO8601Date, graphql_name='startOn')
    end_on = sgqlc.types.Field(ISO8601Date, graphql_name='endOn')


class RemoveAssigneesFromIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'assignee_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')


class RemoveAssigneesFromZenhubEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'assignee_ids', 'zenhub_epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')


class RemoveEpicFromProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'epic_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='epicId')


class RemoveEpicFromRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'epic_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='epicId')


class RemoveEstimateSetValueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class RemoveEstimationVoteInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'estimation_vote_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    estimation_vote_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='estimationVoteId')


class RemoveIssueInfoPrioritiesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssueInfoInput))), graphql_name='issues')


class RemoveIssuesFromEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='epicIds')


class RemoveIssuesFromReleasesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'release_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    release_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='releaseIds')


class RemoveIssuesFromSprintsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'sprint_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    sprint_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='sprintIds')


class RemoveIssuesFromZenhubEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'zenhub_epic_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')


class RemoveLabelsFromIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'label_ids', 'label_infos')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    label_infos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LabelInfoInput)), graphql_name='labelInfos')


class RemoveMilestoneForIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')


class RemoveProjectFromRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'project_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class RemoveRepositoriesFromReleaseInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'repository_gh_ids', 'release_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_gh_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='repositoryGhIds')
    release_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='releaseId')


class RemoveUserFromZenhubOrganizationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_id', 'zenhub_user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId')
    zenhub_user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubUserId')


class RemoveWorkspaceLabelFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_label_filters_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_label_filters_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='workspaceLabelFiltersIds')


class RemoveZenhubAssigneesFromIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'zenhub_user_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    zenhub_user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubUserIds')


class RemoveZenhubEpicFromProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'zenhub_epic_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')


class RemoveZenhubEpicFromRoadmapInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap_id', 'zenhub_epic_id', 'force')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='roadmapId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')
    force = sgqlc.types.Field(Boolean, graphql_name='force')


class RemoveZenhubLabelsFromIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'zenhub_label_ids', 'label_infos')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    zenhub_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='zenhubLabelIds')
    label_infos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LabelInfoInput)), graphql_name='labelInfos')


class RemoveZenhubLabelsFromZenhubEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_ids', 'zenhub_label_ids', 'label_infos')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')
    zenhub_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='zenhubLabelIds')
    label_infos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LabelInfoInput)), graphql_name='labelInfos')


class RemoveZenhubRepositoryFromWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class RemoveZenhubUsersFromWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_user_ids', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubUserIds')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class ReopenIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'pipeline_id', 'position')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')
    position = sgqlc.types.Field(sgqlc.types.non_null(PipelineIssuePosition), graphql_name='position')


class RoadmapItemOrderInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(RoadmapItemOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RoadmapItemStateFilterInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('in_', 'nin')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RoadmapItemState)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RoadmapItemState)), graphql_name='nin')


class SetEstimateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'value', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    value = sgqlc.types.Field(Float, graphql_name='value')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class SetEstimationVoteInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'estimation_vote_id', 'value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    estimation_vote_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='estimationVoteId')
    value = sgqlc.types.Field(Float, graphql_name='value')


class SetFavoriteWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class SetIssueInfoPrioritiesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'priority_id', 'issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    priority_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='priorityId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssueInfoInput))), graphql_name='issues')


class SetMultipleEstimatesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_ids', 'value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    value = sgqlc.types.Field(Float, graphql_name='value')


class SetMultipleEstimatesOnZenhubEpicsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_ids', 'value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds')
    value = sgqlc.types.Field(Float, graphql_name='value')


class SetPipelineStagesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'backlog_pipeline_ids', 'sprint_backlog_pipeline_ids', 'in_development_pipeline_ids', 'in_review_pipeline_ids', 'completed_pipeline_ids', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    backlog_pipeline_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='backlogPipelineIds')
    sprint_backlog_pipeline_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='sprintBacklogPipelineIds')
    in_development_pipeline_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='inDevelopmentPipelineIds')
    in_review_pipeline_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='inReviewPipelineIds')
    completed_pipeline_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='completedPipelineIds')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class SetPriorityOnPipelineIssuesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'priority_id', 'pipeline_issue_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    priority_id = sgqlc.types.Field(ID, graphql_name='priorityId')
    pipeline_issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='pipelineIssueIds')


class SetPullRequestPipelineInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'pipeline_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')


class SetWorkspaceViewedNowInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class SplitWorkspaceRepositoryInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'repository_gh_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    repository_gh_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repositoryGhId')


class SprintConfigCreateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('workspace_id', 'name', 'tz_identifier', 'start_on', 'end_on', 'kind', 'settings')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    tz_identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tzIdentifier')
    start_on = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='startOn')
    end_on = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='endOn')
    kind = sgqlc.types.Field(SprintConfigKind, graphql_name='kind')
    settings = sgqlc.types.Field(sgqlc.types.non_null('SprintConfigSettingsInput'), graphql_name='settings')


class SprintConfigIssuesFromPipelineInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('pipeline_id', 'total_story_points', 'enabled')
    pipeline_id = sgqlc.types.Field(ID, graphql_name='pipelineId')
    total_story_points = sgqlc.types.Field(Float, graphql_name='totalStoryPoints')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class SprintConfigSettingsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('move_unfinished_issues', 'issues_from_pipeline')
    move_unfinished_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='moveUnfinishedIssues')
    issues_from_pipeline = sgqlc.types.Field(sgqlc.types.non_null(SprintConfigIssuesFromPipelineInput), graphql_name='issuesFromPipeline')


class SprintConfigUpdateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('workspace_id', 'name', 'settings', 'tz_identifier', 'start_on', 'end_on', 'kind')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    settings = sgqlc.types.Field(sgqlc.types.non_null(SprintConfigSettingsInput), graphql_name='settings')
    tz_identifier = sgqlc.types.Field(String, graphql_name='tzIdentifier')
    start_on = sgqlc.types.Field(ISO8601Date, graphql_name='startOn')
    end_on = sgqlc.types.Field(ISO8601Date, graphql_name='endOn')
    kind = sgqlc.types.Field(SprintConfigKind, graphql_name='kind')


class SprintFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('state', 'id')
    state = sgqlc.types.Field('SprintStateInput', graphql_name='state')
    id = sgqlc.types.Field('SprintIdInput', graphql_name='id')


class SprintIdInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('not_in_any', 'in_', 'nin', 'special_filters')
    not_in_any = sgqlc.types.Field(Boolean, graphql_name='notInAny')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nin')
    special_filters = sgqlc.types.Field(SprintSpecialFilter, graphql_name='specialFilters')


class SprintOrderInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('direction', 'field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')
    field = sgqlc.types.Field(SprintOrderField, graphql_name='field')


class SprintStateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('eq',)
    eq = sgqlc.types.Field(sgqlc.types.non_null(SprintState), graphql_name='eq')


class StringInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('not_in_any', 'in_', 'nin')
    not_in_any = sgqlc.types.Field(Boolean, graphql_name='notInAny')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')


class UpdateCommentInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'comment_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='commentId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class UpdateEpicDatesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic_id', 'roadmap_id', 'start_on', 'end_on')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='epicId')
    roadmap_id = sgqlc.types.Field(ID, graphql_name='roadmapId')
    start_on = sgqlc.types.Field(ISO8601Date, graphql_name='startOn')
    end_on = sgqlc.types.Field(ISO8601Date, graphql_name='endOn')


class UpdateEpicIssuesByIssueInfosInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic', 'add_issues', 'remove_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null(IssueInfoInput), graphql_name='epic')
    add_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssueInfoInput))), graphql_name='addIssues')
    remove_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssueInfoInput))), graphql_name='removeIssues')


class UpdateIssueInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'body', 'issue_id', 'state', 'title')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    body = sgqlc.types.Field(String, graphql_name='body')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    state = sgqlc.types.Field(IssueState, graphql_name='state')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdatePipelineAutomationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_automation_id', 'element_details')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_automation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineAutomationId')
    element_details = sgqlc.types.Field(JSON, graphql_name='elementDetails')


class UpdatePipelineConfigurationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_id', 'stale_issues', 'stale_interval')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')
    stale_issues = sgqlc.types.Field(Boolean, graphql_name='staleIssues')
    stale_interval = sgqlc.types.Field(Int, graphql_name='staleInterval')


class UpdatePipelineInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_id', 'name', 'position', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineId')
    name = sgqlc.types.Field(String, graphql_name='name')
    position = sgqlc.types.Field(Int, graphql_name='position')
    description = sgqlc.types.Field(String, graphql_name='description')


class UpdateProjectDatesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'start_on', 'end_on', 'action')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    start_on = sgqlc.types.Field(ISO8601Date, graphql_name='startOn')
    end_on = sgqlc.types.Field(ISO8601Date, graphql_name='endOn')
    action = sgqlc.types.Field(sgqlc.types.non_null(ProjectDateAction), graphql_name='action')


class UpdateProjectInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'name', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class UpdateProjectStateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id', 'state', 'apply_to_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    state = sgqlc.types.Field(sgqlc.types.non_null(ProjectState), graphql_name='state')
    apply_to_epics = sgqlc.types.Field(Boolean, graphql_name='applyToEpics')


class UpdateReleaseInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'release_id', 'release')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    release_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='releaseId')
    release = sgqlc.types.Field(sgqlc.types.non_null(ReleaseUpdateInput), graphql_name='release')


class UpdateRoadmapKeyDateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date_id', 'date', 'description', 'color')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='keyDateId')
    date = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='date')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    color = sgqlc.types.Field(String, graphql_name='color')


class UpdateSavedViewInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'saved_view_id', 'name', 'filters')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    saved_view_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='savedViewId')
    name = sgqlc.types.Field(String, graphql_name='name')
    filters = sgqlc.types.Field(IssueSearchFiltersInput, graphql_name='filters')


class UpdateSprintConfigInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_config')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_config = sgqlc.types.Field(sgqlc.types.non_null(SprintConfigUpdateInput), graphql_name='sprintConfig')


class UpdateSprintInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_id', 'name', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sprintId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class UpdateUserPermissionsInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_id', 'zenhub_user_id', 'role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId')
    zenhub_user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubUserId')
    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')


class UpdateWorkspaceInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'name', 'description', 'private', 'are_uploaded_files_private', 'default_repository_gh_id', 'assume_estimates')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    are_uploaded_files_private = sgqlc.types.Field(Boolean, graphql_name='areUploadedFilesPrivate')
    default_repository_gh_id = sgqlc.types.Field(Int, graphql_name='defaultRepositoryGhId')
    assume_estimates = sgqlc.types.Field(Boolean, graphql_name='assumeEstimates')


class UpdateWorkspaceZenhubUserRoleInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id', 'workspace_user_roles')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')
    workspace_user_roles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceRoleInput'))), graphql_name='workspaceUserRoles')


class UpdateZenhubEpicDatesInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_id', 'start_on', 'end_on')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')
    start_on = sgqlc.types.Field(ISO8601Date, graphql_name='startOn')
    end_on = sgqlc.types.Field(ISO8601Date, graphql_name='endOn')


class UpdateZenhubEpicInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_id', 'title', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')


class UpdateZenhubEpicKeyDateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date_id', 'date', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='keyDateId')
    date = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='date')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class UpdateZenhubEpicStateInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_id', 'state', 'apply_to_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')
    state = sgqlc.types.Field(sgqlc.types.non_null(ZenhubEpicState), graphql_name='state')
    apply_to_issues = sgqlc.types.Field(Boolean, graphql_name='applyToIssues')


class UpdateZenhubOrganizationInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization_id', 'address', 'default_payment_method', 'email', 'name', 'name_on_invoice', 'tax_id', 'tax_type_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId')
    address = sgqlc.types.Field(String, graphql_name='address')
    default_payment_method = sgqlc.types.Field(String, graphql_name='defaultPaymentMethod')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_on_invoice = sgqlc.types.Field(String, graphql_name='nameOnInvoice')
    tax_id = sgqlc.types.Field(String, graphql_name='taxId')
    tax_type_id = sgqlc.types.Field(String, graphql_name='taxTypeId')


class WorkspaceOrderInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('direction',)
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')


class WorkspaceRoleInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('zenhub_user_id',)
    zenhub_user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubUserId')


class ZenhubEpicFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('match_type', 'state', 'label_ids', 'project_ids', 'estimate_values', 'assignee_ids', 'id')
    match_type = sgqlc.types.Field(MatchingFilter, graphql_name='matchType')
    state = sgqlc.types.Field('ZenhubEpicStateFilterInput', graphql_name='state')
    label_ids = sgqlc.types.Field(IdInput, graphql_name='labelIds')
    project_ids = sgqlc.types.Field(IdInput, graphql_name='projectIds')
    estimate_values = sgqlc.types.Field(FloatInput, graphql_name='estimateValues')
    assignee_ids = sgqlc.types.Field(IdInput, graphql_name='assigneeIds')
    id = sgqlc.types.Field(IdInput, graphql_name='id')


class ZenhubEpicInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('title', 'body')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')


class ZenhubEpicIssueSearchFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('workspaces',)
    workspaces = sgqlc.types.Field(IdInput, graphql_name='workspaces')


class ZenhubEpicOrderInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('direction', 'field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')
    field = sgqlc.types.Field(ZenhubEpicOrderField, graphql_name='field')


class ZenhubEpicSearchFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'special_filters')
    id = sgqlc.types.Field(IdInput, graphql_name='id')
    special_filters = sgqlc.types.Field(ZenhubEpicSpecialFilter, graphql_name='specialFilters')


class ZenhubEpicStateFilterInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('in_', 'nin')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ZenhubEpicState)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ZenhubEpicState)), graphql_name='nin')


class ZenhubUserOrderInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('direction', 'field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')
    field = sgqlc.types.Field(ZenhubUserOrderField, graphql_name='field')


class ZenhubUsersAssignedEpicsEachSprintCountComparison(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('value', 'sprint_ids')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')
    sprint_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='sprintIds')


class ZenhubUsersAssignedIssuesCountComparison(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('value', 'sprint_ids')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')
    sprint_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='sprintIds')


class ZenhubUsersFiltersInput(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('last_assigned_at_comparison', 'assigned_issues_count_comparison', 'assigned_epics_each_sprint_count_comparison', 'include_external_members')
    last_assigned_at_comparison = sgqlc.types.Field('ZenhubUsersLastAssignedAtComparison', graphql_name='lastAssignedAtComparison')
    assigned_issues_count_comparison = sgqlc.types.Field(ZenhubUsersAssignedIssuesCountComparison, graphql_name='assignedIssuesCountComparison')
    assigned_epics_each_sprint_count_comparison = sgqlc.types.Field(ZenhubUsersAssignedEpicsEachSprintCountComparison, graphql_name='assignedEpicsEachSprintCountComparison')
    include_external_members = sgqlc.types.Field(Boolean, graphql_name='includeExternalMembers')


class ZenhubUsersLastAssignedAtComparison(sgqlc.types.Input):
    __schema__ = zenhub_schema
    __field_names__ = ('value', 'include_nulls', 'sprint_ids')
    value = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='value')
    include_nulls = sgqlc.types.Field(Boolean, graphql_name='includeNulls')
    sprint_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='sprintIds')



########################################################################
# Output Objects and Interfaces
########################################################################
class AcceptZenhubOrganizationInvitePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')


class ActivityFeedConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ActivityFeedEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ActivityFeed'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ActivityFeedEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ActivityFeed', graphql_name='node')


class ActivityFeedField(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('activity_feed',)
    activity_feed = sgqlc.types.Field(ActivityFeedConnection, graphql_name='activityFeed', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('skip_timeline_items', sgqlc.types.Arg(Boolean, graphql_name='skipTimelineItems', default=None)),
))
    )


class AddAssigneesToIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'success_count', 'unassignable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')
    unassignable = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Unassignable'))), graphql_name='unassignable')


class AddAssigneesToZenhubEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class AddEpicsToProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epics', 'previous_projects', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Epic'))), graphql_name='epics')
    previous_projects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='previousProjects')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class AddEpicsToRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epics', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Epic'))), graphql_name='epics')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class AddEstimateSetValuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'estimate_set')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    estimate_set = sgqlc.types.Field(sgqlc.types.non_null('EstimateSet'), graphql_name='estimateSet')


class AddIssuesToEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Epic'))), graphql_name='epics')


class AddIssuesToReleasesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'releases')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    releases = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Release'))), graphql_name='releases')


class AddIssuesToSprintsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintIssue'))), graphql_name='sprintIssues')


class AddIssuesToZenhubEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class AddLabelsToIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'labels', 'success_count')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Label'))), graphql_name='labels')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')


class AddMilestoneForIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'success_count')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')


class AddProjectsToRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'projects', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    projects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Project'))), graphql_name='projects')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class AddRepositoriesToReleasePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'release')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    release = sgqlc.types.Field(sgqlc.types.non_null('Release'), graphql_name='release')


class AddRepositoryToWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_repository = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceRepository'), graphql_name='workspaceRepository')


class AddWorkspaceLabelFiltersPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace', 'workspace_label_filters')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')
    workspace_label_filters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceLabelFilter'))), graphql_name='workspaceLabelFilters')


class AddZenhubAssigneesToIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='issues')


class AddZenhubEpicsToProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'previous_projects', 'project', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    previous_projects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='previousProjects')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class AddZenhubEpicsToRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class AddZenhubLabelsToIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='issues')


class AddZenhubLabelsToZenhubEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class AddZenhubRepositoryToWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_shared_zenhub_repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_shared_zenhub_repository = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceSharedZenhubRepository'), graphql_name='workspaceSharedZenhubRepository')


class AddZenhubUsersToWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace', 'zenhub_users')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')
    zenhub_users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubUser'))), graphql_name='zenhubUsers')


class AnomalousIssue(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('duration', 'issue')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class CloseIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'success_count')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')


class CommentConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CommentEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Comment'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommentEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Comment'), graphql_name='node')


class ConvertZenhubIssueToGithubIssuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class CreateCommentPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateEpicFromIssuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')


class CreateEpicOnProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class CreateEpicOnRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class CreateEpicPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')


class CreateGithubLabelPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'label')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    label = sgqlc.types.Field(sgqlc.types.non_null('Label'), graphql_name='label')


class CreateIssueDependencyPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_dependency')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_dependency = sgqlc.types.Field(sgqlc.types.non_null('IssueDependency'), graphql_name='issueDependency')


class CreateIssuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class CreateIssuePrConnectionPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='pullRequest')


class CreateMilestonePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'milestone')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    milestone = sgqlc.types.Field(sgqlc.types.non_null('Milestone'), graphql_name='milestone')


class CreatePipelineAutomationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_automation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_automation = sgqlc.types.Field(sgqlc.types.non_null('PipelineAutomation'), graphql_name='pipelineAutomation')


class CreatePipelinePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline = sgqlc.types.Field(sgqlc.types.non_null('Pipeline'), graphql_name='pipeline')


class CreatePipelineToPipelineAutomationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'moved_issues_count', 'pipeline_to_pipeline_automation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    moved_issues_count = sgqlc.types.Field(Int, graphql_name='movedIssuesCount')
    pipeline_to_pipeline_automation = sgqlc.types.Field(sgqlc.types.non_null('PipelineToPipelineAutomation'), graphql_name='pipelineToPipelineAutomation')


class CreateProjectOnRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class CreateReleasePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'release')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    release = sgqlc.types.Field(sgqlc.types.non_null('Release'), graphql_name='release')


class CreateRoadmapKeyDatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date = sgqlc.types.Field(sgqlc.types.non_null('KeyDate'), graphql_name='keyDate')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class CreateSavedViewPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'saved_view')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    saved_view = sgqlc.types.Field(sgqlc.types.non_null('SavedView'), graphql_name='savedView')


class CreateSprintConfigPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_config')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_config = sgqlc.types.Field(sgqlc.types.non_null('SprintConfig'), graphql_name='sprintConfig')


class CreateWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class CreateZenhubEpicKeyDatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date = sgqlc.types.Field(sgqlc.types.non_null('KeyDate'), graphql_name='keyDate')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class CreateZenhubEpicOnProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class CreateZenhubEpicOnRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class CreateZenhubEpicPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class CreateZenhubLabelPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_label')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_label = sgqlc.types.Field(sgqlc.types.non_null('ZenhubLabel'), graphql_name='zenhubLabel')


class CreateZenhubOrganizationInvitePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'token')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')


class CreateZenhubOrganizationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')


class DeleteCommentPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteEpicByIssueInfoPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')


class DeleteIssueDependencyPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_dependency')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_dependency = sgqlc.types.Field(sgqlc.types.non_null('IssueDependency'), graphql_name='issueDependency')


class DeleteIssuePrConnectionPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='pullRequest')


class DeleteNotionIntegrationTokenPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'notion_uid', 'zenhub_user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    notion_uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='notionUid')
    zenhub_user = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='zenhubUser')


class DeletePipelineAutomationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_automation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_automation = sgqlc.types.Field(sgqlc.types.non_null('PipelineAutomation'), graphql_name='pipelineAutomation')


class DeletePipelinePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'destination_pipeline')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    destination_pipeline = sgqlc.types.Field(sgqlc.types.non_null('Pipeline'), graphql_name='destinationPipeline')


class DeletePipelineToPipelineAutomationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_to_pipeline_automation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_to_pipeline_automation = sgqlc.types.Field(sgqlc.types.non_null('PipelineToPipelineAutomation'), graphql_name='pipelineToPipelineAutomation')


class DeleteProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class DeleteRoadmapKeyDatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date = sgqlc.types.Field(sgqlc.types.non_null('KeyDate'), graphql_name='keyDate')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class DeleteSavedViewPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'saved_view')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    saved_view = sgqlc.types.Field(sgqlc.types.non_null('SavedView'), graphql_name='savedView')


class DeleteSprintConfigAndOpenSprintsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class DeleteWorkspaceFavoritePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class DeleteWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspaceId')


class DeleteZenhubEpicKeyDatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date = sgqlc.types.Field(sgqlc.types.non_null('KeyDate'), graphql_name='keyDate')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class DeleteZenhubEpicPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubEpicId')


class DeleteZenhubIssuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class DeleteZenhubOrganizationInviteRecipientsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteZenhubOrganizationInvitesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteZenhubUserPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='zenhubUserId')


class DisconnectGithubUserPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_user = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='zenhubUser')


class DisconnectWorkspaceRepositoryPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class DismissConnectNotionPromptPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_user = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='zenhubUser')


class DuplicatePipelineAutomationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_automation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_automation = sgqlc.types.Field(sgqlc.types.non_null('PipelineAutomation'), graphql_name='pipelineAutomation')


class EpicConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EpicEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Epic'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EpicEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='node')


class EstimateSet(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('repository', 'values')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='values')


class EstimationGroup(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'inviter', 'participants', 'workspace')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    inviter = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='inviter')
    participants = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUserConnection'), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('issue_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds', default=None)),
))
    )
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class EstimationGroupConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EstimationGroupEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EstimationGroup))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EstimationGroupEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(EstimationGroup), graphql_name='node')


class EstimationVoteConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EstimationVoteEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EstimationVote'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EstimationVoteEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('EstimationVote'), graphql_name='node')


class GenerateSprintReviewPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_review')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_review = sgqlc.types.Field('SprintReview', graphql_name='sprintReview')


class GithubTimestamps(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('gh_created_at', 'gh_updated_at')
    gh_created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='ghCreatedAt')
    gh_updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='ghUpdatedAt')


class InviteToEstimatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'estimation_votes')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    estimation_votes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EstimationVote'))), graphql_name='estimationVotes')


class IssueConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'pipeline_counts', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    pipeline_counts = sgqlc.types.Field(sgqlc.types.non_null('PipelineCounts'), graphql_name='pipelineCounts')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueCountProgress(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('closed', 'open', 'total')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='closed')
    open = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='open')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class IssueDependencyConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueDependencyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueDependency'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueDependencyEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IssueDependency'), graphql_name='node')


class IssueDependencyItemConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueDependencyItemEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueDependencyItem'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueDependencyItemEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueDependencyItem', graphql_name='node')


class IssueEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='node')


class IssueEstimateProgress(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('closed', 'open', 'total')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='closed')
    open = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='open')
    total = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='total')


class IssueFlowStats(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('anomalies', 'avg_cycle_days', 'in_development_days', 'in_review_days')
    anomalies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AnomalousIssue)), graphql_name='anomalies')
    avg_cycle_days = sgqlc.types.Field(Int, graphql_name='avgCycleDays')
    in_development_days = sgqlc.types.Field(Int, graphql_name='inDevelopmentDays')
    in_review_days = sgqlc.types.Field(Int, graphql_name='inReviewDays')


class IssueLabelOption(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('color', 'name')
    color = sgqlc.types.Field(String, graphql_name='color')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IssueLabelOptionConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabelOptionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssueLabelOption))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueLabelOptionEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelOption), graphql_name='node')


class IssueProgress(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('issue_count_progress', 'issue_estimate_progress')
    issue_count_progress = sgqlc.types.Field(IssueCountProgress, graphql_name='issueCountProgress')
    issue_estimate_progress = sgqlc.types.Field(IssueEstimateProgress, graphql_name='issueEstimateProgress')


class IssueTemplate(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('body', 'default', 'id', 'metadata', 'path', 'raw', 'repository')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='default')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    metadata = sgqlc.types.Field(JSON, graphql_name='metadata')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    raw = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='raw')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class IssueTemplateConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueTemplateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssueTemplate))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueTemplateEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(IssueTemplate), graphql_name='node')


class IssueUserOption(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('github_user', 'zenhub_user')
    github_user = sgqlc.types.Field('User', graphql_name='githubUser')
    zenhub_user = sgqlc.types.Field('ZenhubUser', graphql_name='zenhubUser')


class IssueUserOptionConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueUserOptionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssueUserOption))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueUserOptionEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(IssueUserOption), graphql_name='node')


class KeyDateConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyDateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyDate'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class KeyDateEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('KeyDate'), graphql_name='node')


class LabelConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LabelEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Label'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LabelEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Label'), graphql_name='node')


class LeaveZenhubOrganizationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')


class MilestoneConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MilestoneEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Milestone'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MilestoneEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Milestone'), graphql_name='node')


class MoveAllPipelineIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class MoveIssuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue', 'pipeline')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    pipeline = sgqlc.types.Field(sgqlc.types.non_null('Pipeline'), graphql_name='pipeline')


class MoveIssueRelativeToPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_issue_move')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_issue_move = sgqlc.types.Field(sgqlc.types.non_null('PipelineIssueMove'), graphql_name='pipelineIssueMove')


class MovePipelineIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline', 'pipeline_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline = sgqlc.types.Field(sgqlc.types.non_null('Pipeline'), graphql_name='pipeline')
    pipeline_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineIssue'))), graphql_name='pipelineIssues')


class MoveRoadmapItemRelativeToPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item = sgqlc.types.Field(sgqlc.types.non_null('RoadmapItem'), graphql_name='item')


class MoveZenhubIssueToWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class Mutation(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('accept_zenhub_organization_invite', 'add_assignees_to_issues', 'add_assignees_to_zenhub_epics', 'add_estimate_set_value', 'add_issues_to_releases', 'add_issues_to_sprints', 'add_issues_to_zenhub_epics', 'add_labels_to_issues', 'add_milestone_to_issues', 'add_projects_to_roadmap', 'add_repositories_to_release', 'add_repository_to_workspace', 'add_workspace_label_filters', 'add_zenhub_assignees_to_issues', 'add_zenhub_epics_to_project', 'add_zenhub_epics_to_roadmap', 'add_zenhub_labels_to_issues', 'add_zenhub_labels_to_zenhub_epics', 'add_zenhub_repository_to_workspace', 'add_zenhub_users_to_workspace', 'close_issues', 'convert_zenhub_issue_to_github_issue', 'create_comment', 'create_github_label', 'create_issue', 'create_issue_pr_connection', 'create_milestone', 'create_pipeline', 'create_pipeline_automation', 'create_pipeline_to_pipeline_automation', 'create_project_on_roadmap', 'create_release', 'create_roadmap_key_date', 'create_saved_view', 'create_sprint_config', 'create_workspace', 'create_zenhub_epic', 'create_zenhub_epic_key_date', 'create_zenhub_epic_on_project', 'create_zenhub_epic_on_roadmap', 'create_zenhub_label', 'create_zenhub_organization', 'create_zenhub_organization_invite', 'delete_comment', 'delete_issue_pr_connection', 'delete_notion_integration_token', 'delete_pipeline', 'delete_pipeline_automation', 'delete_pipeline_to_pipeline_automation', 'delete_project', 'delete_roadmap_key_date', 'delete_saved_view', 'delete_sprint_config_and_open_sprints', 'delete_workspace', 'delete_workspace_favorite', 'delete_zenhub_epic', 'delete_zenhub_epic_key_date', 'delete_zenhub_issue', 'delete_zenhub_organization_invite_recipients', 'delete_zenhub_organization_invites', 'delete_zenhub_user', 'disconnect_github_user', 'disconnect_workspace_repository', 'dismiss_connect_notion_prompt', 'duplicate_pipeline_automation', 'generate_sprint_review', 'invite_to_estimate', 'leave_zenhub_organization', 'move_all_pipeline_issues', 'move_issue', 'move_issue_relative_to', 'move_pipeline_issues', 'move_roadmap_item_relative_to', 'move_zenhub_issue_to_workspace', 'remove_assignees_from_issues', 'remove_assignees_from_zenhub_epics', 'remove_estimate_set_value', 'remove_estimation_vote', 'remove_issue_info_priorities', 'remove_issues_from_releases', 'remove_issues_from_sprints', 'remove_issues_from_zenhub_epics', 'remove_labels_from_issues', 'remove_milestone_to_issues', 'remove_project_from_roadmap', 'remove_repositories_from_release', 'remove_user_from_zenhub_organization', 'remove_workspace_label_filters', 'remove_zenhub_assignees_from_issues', 'remove_zenhub_epic_from_project', 'remove_zenhub_epic_from_roadmap', 'remove_zenhub_labels_from_issues', 'remove_zenhub_labels_from_zenhub_epics', 'remove_zenhub_repository_from_workspace', 'remove_zenhub_users_from_workspace', 'reopen_issues', 'set_estimate', 'set_estimation_vote', 'set_favorite_workspace', 'set_issue_info_priorities', 'set_multiple_estimates', 'set_multiple_estimates_on_zenhub_epics', 'set_pipeline_stages', 'set_priority_on_pipeline_issues', 'set_pull_request_pipeline', 'set_workspace_viewed_now', 'split_workspace_repository', 'update_comment', 'update_issue', 'update_pipeline', 'update_pipeline_automation', 'update_pipeline_configuration', 'update_project', 'update_project_dates', 'update_project_state', 'update_release', 'update_roadmap_key_date', 'update_saved_view', 'update_sprint', 'update_sprint_config', 'update_user_permissions', 'update_workspace', 'update_workspace_zenhub_user_role', 'update_zenhub_epic', 'update_zenhub_epic_dates', 'update_zenhub_epic_key_date', 'update_zenhub_epic_state', 'update_zenhub_organization')
    accept_zenhub_organization_invite = sgqlc.types.Field(AcceptZenhubOrganizationInvitePayload, graphql_name='acceptZenhubOrganizationInvite', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AcceptZenhubOrganizationInviteInput), graphql_name='input', default=None)),
))
    )
    add_assignees_to_issues = sgqlc.types.Field(AddAssigneesToIssuesPayload, graphql_name='addAssigneesToIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddAssigneesToIssuesInput), graphql_name='input', default=None)),
))
    )
    add_assignees_to_zenhub_epics = sgqlc.types.Field(AddAssigneesToZenhubEpicsPayload, graphql_name='addAssigneesToZenhubEpics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddAssigneesToZenhubEpicsInput), graphql_name='input', default=None)),
))
    )
    add_estimate_set_value = sgqlc.types.Field(AddEstimateSetValuePayload, graphql_name='addEstimateSetValue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddEstimateSetValueInput), graphql_name='input', default=None)),
))
    )
    add_issues_to_releases = sgqlc.types.Field(AddIssuesToReleasesPayload, graphql_name='addIssuesToReleases', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddIssuesToReleasesInput), graphql_name='input', default=None)),
))
    )
    add_issues_to_sprints = sgqlc.types.Field(AddIssuesToSprintsPayload, graphql_name='addIssuesToSprints', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddIssuesToSprintsInput), graphql_name='input', default=None)),
))
    )
    add_issues_to_zenhub_epics = sgqlc.types.Field(AddIssuesToZenhubEpicsPayload, graphql_name='addIssuesToZenhubEpics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddIssuesToZenhubEpicsInput), graphql_name='input', default=None)),
))
    )
    add_labels_to_issues = sgqlc.types.Field(AddLabelsToIssuesPayload, graphql_name='addLabelsToIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddLabelsToIssuesInput), graphql_name='input', default=None)),
))
    )
    add_milestone_to_issues = sgqlc.types.Field(AddMilestoneForIssuesPayload, graphql_name='addMilestoneToIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddMilestoneForIssuesInput), graphql_name='input', default=None)),
))
    )
    add_projects_to_roadmap = sgqlc.types.Field(AddProjectsToRoadmapPayload, graphql_name='addProjectsToRoadmap', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectsToRoadmapInput), graphql_name='input', default=None)),
))
    )
    add_repositories_to_release = sgqlc.types.Field(AddRepositoriesToReleasePayload, graphql_name='addRepositoriesToRelease', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddRepositoriesToReleaseInput), graphql_name='input', default=None)),
))
    )
    add_repository_to_workspace = sgqlc.types.Field(AddRepositoryToWorkspacePayload, graphql_name='addRepositoryToWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddRepositoryToWorkspaceInput), graphql_name='input', default=None)),
))
    )
    add_workspace_label_filters = sgqlc.types.Field(AddWorkspaceLabelFiltersPayload, graphql_name='addWorkspaceLabelFilters', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddWorkspaceLabelFiltersInput), graphql_name='input', default=None)),
))
    )
    add_zenhub_assignees_to_issues = sgqlc.types.Field(AddZenhubAssigneesToIssuesPayload, graphql_name='addZenhubAssigneesToIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddZenhubAssigneesToIssuesInput), graphql_name='input', default=None)),
))
    )
    add_zenhub_epics_to_project = sgqlc.types.Field(AddZenhubEpicsToProjectPayload, graphql_name='addZenhubEpicsToProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddZenhubEpicsToProjectInput), graphql_name='input', default=None)),
))
    )
    add_zenhub_epics_to_roadmap = sgqlc.types.Field(AddZenhubEpicsToRoadmapPayload, graphql_name='addZenhubEpicsToRoadmap', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddZenhubEpicsToRoadmapInput), graphql_name='input', default=None)),
))
    )
    add_zenhub_labels_to_issues = sgqlc.types.Field(AddZenhubLabelsToIssuesPayload, graphql_name='addZenhubLabelsToIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddZenhubLabelsToIssuesInput), graphql_name='input', default=None)),
))
    )
    add_zenhub_labels_to_zenhub_epics = sgqlc.types.Field(AddZenhubLabelsToZenhubEpicsPayload, graphql_name='addZenhubLabelsToZenhubEpics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddZenhubLabelsToZenhubEpicsInput), graphql_name='input', default=None)),
))
    )
    add_zenhub_repository_to_workspace = sgqlc.types.Field(AddZenhubRepositoryToWorkspacePayload, graphql_name='addZenhubRepositoryToWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddZenhubRepositoryToWorkspaceInput), graphql_name='input', default=None)),
))
    )
    add_zenhub_users_to_workspace = sgqlc.types.Field(AddZenhubUsersToWorkspacePayload, graphql_name='addZenhubUsersToWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddZenhubUsersToWorkspaceInput), graphql_name='input', default=None)),
))
    )
    close_issues = sgqlc.types.Field(CloseIssuesPayload, graphql_name='closeIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CloseIssuesInput), graphql_name='input', default=None)),
))
    )
    convert_zenhub_issue_to_github_issue = sgqlc.types.Field(ConvertZenhubIssueToGithubIssuePayload, graphql_name='convertZenhubIssueToGithubIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConvertZenhubIssueToGithubIssueInput), graphql_name='input', default=None)),
))
    )
    create_comment = sgqlc.types.Field(CreateCommentPayload, graphql_name='createComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCommentInput), graphql_name='input', default=None)),
))
    )
    create_github_label = sgqlc.types.Field(CreateGithubLabelPayload, graphql_name='createGithubLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateGithubLabelInput), graphql_name='input', default=None)),
))
    )
    create_issue = sgqlc.types.Field(CreateIssuePayload, graphql_name='createIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateIssueInput), graphql_name='input', default=None)),
))
    )
    create_issue_pr_connection = sgqlc.types.Field(CreateIssuePrConnectionPayload, graphql_name='createIssuePrConnection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateIssuePrConnectionInput), graphql_name='input', default=None)),
))
    )
    create_milestone = sgqlc.types.Field(CreateMilestonePayload, graphql_name='createMilestone', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMilestoneInput), graphql_name='input', default=None)),
))
    )
    create_pipeline = sgqlc.types.Field(CreatePipelinePayload, graphql_name='createPipeline', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePipelineInput), graphql_name='input', default=None)),
))
    )
    create_pipeline_automation = sgqlc.types.Field(CreatePipelineAutomationPayload, graphql_name='createPipelineAutomation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePipelineAutomationInput), graphql_name='input', default=None)),
))
    )
    create_pipeline_to_pipeline_automation = sgqlc.types.Field(CreatePipelineToPipelineAutomationPayload, graphql_name='createPipelineToPipelineAutomation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePipelineToPipelineAutomationInput), graphql_name='input', default=None)),
))
    )
    create_project_on_roadmap = sgqlc.types.Field(CreateProjectOnRoadmapPayload, graphql_name='createProjectOnRoadmap', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectOnRoadmapInput), graphql_name='input', default=None)),
))
    )
    create_release = sgqlc.types.Field(CreateReleasePayload, graphql_name='createRelease', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateReleaseInput), graphql_name='input', default=None)),
))
    )
    create_roadmap_key_date = sgqlc.types.Field(CreateRoadmapKeyDatePayload, graphql_name='createRoadmapKeyDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRoadmapKeyDateInput), graphql_name='input', default=None)),
))
    )
    create_saved_view = sgqlc.types.Field(CreateSavedViewPayload, graphql_name='createSavedView', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSavedViewInput), graphql_name='input', default=None)),
))
    )
    create_sprint_config = sgqlc.types.Field(CreateSprintConfigPayload, graphql_name='createSprintConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSprintConfigInput), graphql_name='input', default=None)),
))
    )
    create_workspace = sgqlc.types.Field(CreateWorkspacePayload, graphql_name='createWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateWorkspaceInput), graphql_name='input', default=None)),
))
    )
    create_zenhub_epic = sgqlc.types.Field(CreateZenhubEpicPayload, graphql_name='createZenhubEpic', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateZenhubEpicInput), graphql_name='input', default=None)),
))
    )
    create_zenhub_epic_key_date = sgqlc.types.Field(CreateZenhubEpicKeyDatePayload, graphql_name='createZenhubEpicKeyDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateZenhubEpicKeyDateInput), graphql_name='input', default=None)),
))
    )
    create_zenhub_epic_on_project = sgqlc.types.Field(CreateZenhubEpicOnProjectPayload, graphql_name='createZenhubEpicOnProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateZenhubEpicOnProjectInput), graphql_name='input', default=None)),
))
    )
    create_zenhub_epic_on_roadmap = sgqlc.types.Field(CreateZenhubEpicOnRoadmapPayload, graphql_name='createZenhubEpicOnRoadmap', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateZenhubEpicOnRoadmapInput), graphql_name='input', default=None)),
))
    )
    create_zenhub_label = sgqlc.types.Field(CreateZenhubLabelPayload, graphql_name='createZenhubLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateZenhubLabelInput), graphql_name='input', default=None)),
))
    )
    create_zenhub_organization = sgqlc.types.Field(CreateZenhubOrganizationPayload, graphql_name='createZenhubOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateZenhubOrganizationInput), graphql_name='input', default=None)),
))
    )
    create_zenhub_organization_invite = sgqlc.types.Field(CreateZenhubOrganizationInvitePayload, graphql_name='createZenhubOrganizationInvite', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateZenhubOrganizationInviteInput), graphql_name='input', default=None)),
))
    )
    delete_comment = sgqlc.types.Field(DeleteCommentPayload, graphql_name='deleteComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCommentInput), graphql_name='input', default=None)),
))
    )
    delete_issue_pr_connection = sgqlc.types.Field(DeleteIssuePrConnectionPayload, graphql_name='deleteIssuePrConnection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteIssuePrConnectionInput), graphql_name='input', default=None)),
))
    )
    delete_notion_integration_token = sgqlc.types.Field(DeleteNotionIntegrationTokenPayload, graphql_name='deleteNotionIntegrationToken', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteNotionIntegrationTokenInput), graphql_name='input', default=None)),
))
    )
    delete_pipeline = sgqlc.types.Field(DeletePipelinePayload, graphql_name='deletePipeline', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePipelineInput), graphql_name='input', default=None)),
))
    )
    delete_pipeline_automation = sgqlc.types.Field(DeletePipelineAutomationPayload, graphql_name='deletePipelineAutomation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePipelineAutomationInput), graphql_name='input', default=None)),
))
    )
    delete_pipeline_to_pipeline_automation = sgqlc.types.Field(DeletePipelineToPipelineAutomationPayload, graphql_name='deletePipelineToPipelineAutomation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePipelineToPipelineAutomationInput), graphql_name='input', default=None)),
))
    )
    delete_project = sgqlc.types.Field(DeleteProjectPayload, graphql_name='deleteProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectInput), graphql_name='input', default=None)),
))
    )
    delete_roadmap_key_date = sgqlc.types.Field(DeleteRoadmapKeyDatePayload, graphql_name='deleteRoadmapKeyDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteRoadmapKeyDateInput), graphql_name='input', default=None)),
))
    )
    delete_saved_view = sgqlc.types.Field(DeleteSavedViewPayload, graphql_name='deleteSavedView', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteSavedViewInput), graphql_name='input', default=None)),
))
    )
    delete_sprint_config_and_open_sprints = sgqlc.types.Field(DeleteSprintConfigAndOpenSprintsPayload, graphql_name='deleteSprintConfigAndOpenSprints', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteSprintConfigAndOpenSprintsInput), graphql_name='input', default=None)),
))
    )
    delete_workspace = sgqlc.types.Field(DeleteWorkspacePayload, graphql_name='deleteWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteWorkspaceInput), graphql_name='input', default=None)),
))
    )
    delete_workspace_favorite = sgqlc.types.Field(DeleteWorkspaceFavoritePayload, graphql_name='deleteWorkspaceFavorite', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteWorkspaceFavoriteInput), graphql_name='input', default=None)),
))
    )
    delete_zenhub_epic = sgqlc.types.Field(DeleteZenhubEpicPayload, graphql_name='deleteZenhubEpic', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteZenhubEpicInput), graphql_name='input', default=None)),
))
    )
    delete_zenhub_epic_key_date = sgqlc.types.Field(DeleteZenhubEpicKeyDatePayload, graphql_name='deleteZenhubEpicKeyDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteZenhubEpicKeyDateInput), graphql_name='input', default=None)),
))
    )
    delete_zenhub_issue = sgqlc.types.Field(DeleteZenhubIssuePayload, graphql_name='deleteZenhubIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteZenhubIssueInput), graphql_name='input', default=None)),
))
    )
    delete_zenhub_organization_invite_recipients = sgqlc.types.Field(DeleteZenhubOrganizationInviteRecipientsPayload, graphql_name='deleteZenhubOrganizationInviteRecipients', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteZenhubOrganizationInviteRecipientsInput), graphql_name='input', default=None)),
))
    )
    delete_zenhub_organization_invites = sgqlc.types.Field(DeleteZenhubOrganizationInvitesPayload, graphql_name='deleteZenhubOrganizationInvites', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteZenhubOrganizationInvitesInput), graphql_name='input', default=None)),
))
    )
    delete_zenhub_user = sgqlc.types.Field(DeleteZenhubUserPayload, graphql_name='deleteZenhubUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteZenhubUserInput), graphql_name='input', default=None)),
))
    )
    disconnect_github_user = sgqlc.types.Field(DisconnectGithubUserPayload, graphql_name='disconnectGithubUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DisconnectGithubUserInput), graphql_name='input', default=None)),
))
    )
    disconnect_workspace_repository = sgqlc.types.Field(DisconnectWorkspaceRepositoryPayload, graphql_name='disconnectWorkspaceRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DisconnectWorkspaceRepositoryInput), graphql_name='input', default=None)),
))
    )
    dismiss_connect_notion_prompt = sgqlc.types.Field(DismissConnectNotionPromptPayload, graphql_name='dismissConnectNotionPrompt', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DismissConnectNotionPromptInput), graphql_name='input', default=None)),
))
    )
    duplicate_pipeline_automation = sgqlc.types.Field(DuplicatePipelineAutomationPayload, graphql_name='duplicatePipelineAutomation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DuplicatePipelineAutomationInput), graphql_name='input', default=None)),
))
    )
    generate_sprint_review = sgqlc.types.Field(GenerateSprintReviewPayload, graphql_name='generateSprintReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GenerateSprintReviewInput), graphql_name='input', default=None)),
))
    )
    invite_to_estimate = sgqlc.types.Field(InviteToEstimatePayload, graphql_name='inviteToEstimate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InviteToEstimateInput), graphql_name='input', default=None)),
))
    )
    leave_zenhub_organization = sgqlc.types.Field(LeaveZenhubOrganizationPayload, graphql_name='leaveZenhubOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LeaveZenhubOrganizationInput), graphql_name='input', default=None)),
))
    )
    move_all_pipeline_issues = sgqlc.types.Field(MoveAllPipelineIssuesPayload, graphql_name='moveAllPipelineIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveAllPipelineIssuesInput), graphql_name='input', default=None)),
))
    )
    move_issue = sgqlc.types.Field(MoveIssuePayload, graphql_name='moveIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveIssueInput), graphql_name='input', default=None)),
))
    )
    move_issue_relative_to = sgqlc.types.Field(MoveIssueRelativeToPayload, graphql_name='moveIssueRelativeTo', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveIssueRelativeToInput), graphql_name='input', default=None)),
))
    )
    move_pipeline_issues = sgqlc.types.Field(MovePipelineIssuesPayload, graphql_name='movePipelineIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MovePipelineIssuesInput), graphql_name='input', default=None)),
))
    )
    move_roadmap_item_relative_to = sgqlc.types.Field(MoveRoadmapItemRelativeToPayload, graphql_name='moveRoadmapItemRelativeTo', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveRoadmapItemRelativeToInput), graphql_name='input', default=None)),
))
    )
    move_zenhub_issue_to_workspace = sgqlc.types.Field(MoveZenhubIssueToWorkspacePayload, graphql_name='moveZenhubIssueToWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveZenhubIssueToWorkspaceInput), graphql_name='input', default=None)),
))
    )
    remove_assignees_from_issues = sgqlc.types.Field('RemoveAssigneesFromIssuesPayload', graphql_name='removeAssigneesFromIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveAssigneesFromIssuesInput), graphql_name='input', default=None)),
))
    )
    remove_assignees_from_zenhub_epics = sgqlc.types.Field('RemoveAssigneesFromZenhubEpicsPayload', graphql_name='removeAssigneesFromZenhubEpics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveAssigneesFromZenhubEpicsInput), graphql_name='input', default=None)),
))
    )
    remove_estimate_set_value = sgqlc.types.Field('RemoveEstimateSetValuePayload', graphql_name='removeEstimateSetValue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEstimateSetValueInput), graphql_name='input', default=None)),
))
    )
    remove_estimation_vote = sgqlc.types.Field('RemoveEstimationVotePayload', graphql_name='removeEstimationVote', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEstimationVoteInput), graphql_name='input', default=None)),
))
    )
    remove_issue_info_priorities = sgqlc.types.Field('RemoveIssueInfoPrioritiesPayload', graphql_name='removeIssueInfoPriorities', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveIssueInfoPrioritiesInput), graphql_name='input', default=None)),
))
    )
    remove_issues_from_releases = sgqlc.types.Field('RemoveIssuesFromReleasesPayload', graphql_name='removeIssuesFromReleases', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveIssuesFromReleasesInput), graphql_name='input', default=None)),
))
    )
    remove_issues_from_sprints = sgqlc.types.Field('RemoveIssuesFromSprintsPayload', graphql_name='removeIssuesFromSprints', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveIssuesFromSprintsInput), graphql_name='input', default=None)),
))
    )
    remove_issues_from_zenhub_epics = sgqlc.types.Field('RemoveIssuesFromZenhubEpicsPayload', graphql_name='removeIssuesFromZenhubEpics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveIssuesFromZenhubEpicsInput), graphql_name='input', default=None)),
))
    )
    remove_labels_from_issues = sgqlc.types.Field('RemoveLabelsFromIssuesPayload', graphql_name='removeLabelsFromIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveLabelsFromIssuesInput), graphql_name='input', default=None)),
))
    )
    remove_milestone_to_issues = sgqlc.types.Field('RemoveMilestoneForIssuesPayload', graphql_name='removeMilestoneToIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveMilestoneForIssuesInput), graphql_name='input', default=None)),
))
    )
    remove_project_from_roadmap = sgqlc.types.Field('RemoveProjectFromRoadmapPayload', graphql_name='removeProjectFromRoadmap', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveProjectFromRoadmapInput), graphql_name='input', default=None)),
))
    )
    remove_repositories_from_release = sgqlc.types.Field('RemoveRepositoriesFromReleasePayload', graphql_name='removeRepositoriesFromRelease', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveRepositoriesFromReleaseInput), graphql_name='input', default=None)),
))
    )
    remove_user_from_zenhub_organization = sgqlc.types.Field('RemoveUserFromZenhubOrganizationPayload', graphql_name='removeUserFromZenhubOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveUserFromZenhubOrganizationInput), graphql_name='input', default=None)),
))
    )
    remove_workspace_label_filters = sgqlc.types.Field('RemoveWorkspaceLabelFiltersPayload', graphql_name='removeWorkspaceLabelFilters', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveWorkspaceLabelFiltersInput), graphql_name='input', default=None)),
))
    )
    remove_zenhub_assignees_from_issues = sgqlc.types.Field('RemoveZenhubAssigneesFromIssuesPayload', graphql_name='removeZenhubAssigneesFromIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveZenhubAssigneesFromIssuesInput), graphql_name='input', default=None)),
))
    )
    remove_zenhub_epic_from_project = sgqlc.types.Field('RemoveZenhubEpicFromProjectPayload', graphql_name='removeZenhubEpicFromProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveZenhubEpicFromProjectInput), graphql_name='input', default=None)),
))
    )
    remove_zenhub_epic_from_roadmap = sgqlc.types.Field('RemoveZenhubEpicFromRoadmapPayload', graphql_name='removeZenhubEpicFromRoadmap', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveZenhubEpicFromRoadmapInput), graphql_name='input', default=None)),
))
    )
    remove_zenhub_labels_from_issues = sgqlc.types.Field('RemoveZenhubLabelsFromIssuesPayload', graphql_name='removeZenhubLabelsFromIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveZenhubLabelsFromIssuesInput), graphql_name='input', default=None)),
))
    )
    remove_zenhub_labels_from_zenhub_epics = sgqlc.types.Field('RemoveZenhubLabelsFromZenhubEpicsPayload', graphql_name='removeZenhubLabelsFromZenhubEpics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveZenhubLabelsFromZenhubEpicsInput), graphql_name='input', default=None)),
))
    )
    remove_zenhub_repository_from_workspace = sgqlc.types.Field('RemoveZenhubRepositoryFromWorkspacePayload', graphql_name='removeZenhubRepositoryFromWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveZenhubRepositoryFromWorkspaceInput), graphql_name='input', default=None)),
))
    )
    remove_zenhub_users_from_workspace = sgqlc.types.Field('RemoveZenhubUsersFromWorkspacePayload', graphql_name='removeZenhubUsersFromWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveZenhubUsersFromWorkspaceInput), graphql_name='input', default=None)),
))
    )
    reopen_issues = sgqlc.types.Field('ReopenIssuesPayload', graphql_name='reopenIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReopenIssuesInput), graphql_name='input', default=None)),
))
    )
    set_estimate = sgqlc.types.Field('SetEstimatePayload', graphql_name='setEstimate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetEstimateInput), graphql_name='input', default=None)),
))
    )
    set_estimation_vote = sgqlc.types.Field('SetEstimationVotePayload', graphql_name='setEstimationVote', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetEstimationVoteInput), graphql_name='input', default=None)),
))
    )
    set_favorite_workspace = sgqlc.types.Field('SetFavoriteWorkspacePayload', graphql_name='setFavoriteWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetFavoriteWorkspaceInput), graphql_name='input', default=None)),
))
    )
    set_issue_info_priorities = sgqlc.types.Field('SetIssueInfoPrioritiesPayload', graphql_name='setIssueInfoPriorities', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetIssueInfoPrioritiesInput), graphql_name='input', default=None)),
))
    )
    set_multiple_estimates = sgqlc.types.Field('SetMultipleEstimatesPayload', graphql_name='setMultipleEstimates', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetMultipleEstimatesInput), graphql_name='input', default=None)),
))
    )
    set_multiple_estimates_on_zenhub_epics = sgqlc.types.Field('SetMultipleEstimatesOnZenhubEpicsPayload', graphql_name='setMultipleEstimatesOnZenhubEpics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetMultipleEstimatesOnZenhubEpicsInput), graphql_name='input', default=None)),
))
    )
    set_pipeline_stages = sgqlc.types.Field('SetPipelineStagesPayload', graphql_name='setPipelineStages', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetPipelineStagesInput), graphql_name='input', default=None)),
))
    )
    set_priority_on_pipeline_issues = sgqlc.types.Field('SetPriorityOnPipelineIssuesPayload', graphql_name='setPriorityOnPipelineIssues', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetPriorityOnPipelineIssuesInput), graphql_name='input', default=None)),
))
    )
    set_pull_request_pipeline = sgqlc.types.Field('SetPullRequestPipelinePayload', graphql_name='setPullRequestPipeline', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetPullRequestPipelineInput), graphql_name='input', default=None)),
))
    )
    set_workspace_viewed_now = sgqlc.types.Field('SetWorkspaceViewedNowPayload', graphql_name='setWorkspaceViewedNow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetWorkspaceViewedNowInput), graphql_name='input', default=None)),
))
    )
    split_workspace_repository = sgqlc.types.Field('SplitWorkspaceRepositoryPayload', graphql_name='splitWorkspaceRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SplitWorkspaceRepositoryInput), graphql_name='input', default=None)),
))
    )
    update_comment = sgqlc.types.Field('UpdateCommentPayload', graphql_name='updateComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCommentInput), graphql_name='input', default=None)),
))
    )
    update_issue = sgqlc.types.Field('UpdateIssuePayload', graphql_name='updateIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIssueInput), graphql_name='input', default=None)),
))
    )
    update_pipeline = sgqlc.types.Field('UpdatePipelinePayload', graphql_name='updatePipeline', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePipelineInput), graphql_name='input', default=None)),
))
    )
    update_pipeline_automation = sgqlc.types.Field('UpdatePipelineAutomationPayload', graphql_name='updatePipelineAutomation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePipelineAutomationInput), graphql_name='input', default=None)),
))
    )
    update_pipeline_configuration = sgqlc.types.Field('UpdatePipelineConfigurationPayload', graphql_name='updatePipelineConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePipelineConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_project = sgqlc.types.Field('UpdateProjectPayload', graphql_name='updateProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectInput), graphql_name='input', default=None)),
))
    )
    update_project_dates = sgqlc.types.Field('UpdateProjectDatesPayload', graphql_name='updateProjectDates', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectDatesInput), graphql_name='input', default=None)),
))
    )
    update_project_state = sgqlc.types.Field('UpdateProjectStatePayload', graphql_name='updateProjectState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectStateInput), graphql_name='input', default=None)),
))
    )
    update_release = sgqlc.types.Field('UpdateReleasePayload', graphql_name='updateRelease', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateReleaseInput), graphql_name='input', default=None)),
))
    )
    update_roadmap_key_date = sgqlc.types.Field('UpdateRoadmapKeyDatePayload', graphql_name='updateRoadmapKeyDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRoadmapKeyDateInput), graphql_name='input', default=None)),
))
    )
    update_saved_view = sgqlc.types.Field('UpdateSavedViewPayload', graphql_name='updateSavedView', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSavedViewInput), graphql_name='input', default=None)),
))
    )
    update_sprint = sgqlc.types.Field('UpdateSprintPayload', graphql_name='updateSprint', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSprintInput), graphql_name='input', default=None)),
))
    )
    update_sprint_config = sgqlc.types.Field('UpdateSprintConfigPayload', graphql_name='updateSprintConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSprintConfigInput), graphql_name='input', default=None)),
))
    )
    update_user_permissions = sgqlc.types.Field('UpdateUserPermissionsPayload', graphql_name='updateUserPermissions', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserPermissionsInput), graphql_name='input', default=None)),
))
    )
    update_workspace = sgqlc.types.Field('UpdateWorkspacePayload', graphql_name='updateWorkspace', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkspaceInput), graphql_name='input', default=None)),
))
    )
    update_workspace_zenhub_user_role = sgqlc.types.Field('UpdateWorkspaceZenhubUserRolePayload', graphql_name='updateWorkspaceZenhubUserRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkspaceZenhubUserRoleInput), graphql_name='input', default=None)),
))
    )
    update_zenhub_epic = sgqlc.types.Field('UpdateZenhubEpicPayload', graphql_name='updateZenhubEpic', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateZenhubEpicInput), graphql_name='input', default=None)),
))
    )
    update_zenhub_epic_dates = sgqlc.types.Field('UpdateZenhubEpicDatesPayload', graphql_name='updateZenhubEpicDates', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateZenhubEpicDatesInput), graphql_name='input', default=None)),
))
    )
    update_zenhub_epic_key_date = sgqlc.types.Field('UpdateZenhubEpicKeyDatePayload', graphql_name='updateZenhubEpicKeyDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateZenhubEpicKeyDateInput), graphql_name='input', default=None)),
))
    )
    update_zenhub_epic_state = sgqlc.types.Field('UpdateZenhubEpicStatePayload', graphql_name='updateZenhubEpicState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateZenhubEpicStateInput), graphql_name='input', default=None)),
))
    )
    update_zenhub_organization = sgqlc.types.Field('UpdateZenhubOrganizationPayload', graphql_name='updateZenhubOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateZenhubOrganizationInput), graphql_name='input', default=None)),
))
    )


class Node(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Owner(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('avatar_url', 'created_at', 'gh_id', 'has_workspace', 'id', 'login', 'projects', 'repository_favorites', 'roadmap_items', 'search_workspaces', 'type', 'updated_at', 'workspace_favorites')
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='avatarUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    gh_id = sgqlc.types.Field(Int, graphql_name='ghId')
    has_workspace = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWorkspace')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    projects = sgqlc.types.Field(sgqlc.types.non_null('ProjectConnection'), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository_favorites = sgqlc.types.Field(sgqlc.types.non_null('RepositoryFavoriteConnection'), graphql_name='repositoryFavorites', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    roadmap_items = sgqlc.types.Field(sgqlc.types.non_null('RoadmapItemConnection'), graphql_name='roadmapItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(RoadmapItemStateFilterInput, graphql_name='state', default=None)),
))
    )
    search_workspaces = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceSearchMatchConnection'), graphql_name='searchWorkspaces', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('repository_gh_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='repositoryGhIds', default=None)),
))
    )
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')
    workspace_favorites = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceFavoriteConnection'), graphql_name='workspaceFavorites', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class PageInfo(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')


class PipelineAutomationConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineAutomationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineAutomation'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PipelineAutomationEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PipelineAutomation'), graphql_name='node')


class PipelineConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Pipeline'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PipelineCounts(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('issues_count', 'pull_requests_count', 'sum_estimates', 'unfiltered_issue_count', 'unfiltered_sum_estimates')
    issues_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issuesCount')
    pull_requests_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pullRequestsCount')
    sum_estimates = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sumEstimates')
    unfiltered_issue_count = sgqlc.types.Field(Int, graphql_name='unfilteredIssueCount')
    unfiltered_sum_estimates = sgqlc.types.Field(Float, graphql_name='unfilteredSumEstimates')


class PipelineEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Pipeline'), graphql_name='node')


class PipelineIssue(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'issue', 'item_after', 'item_before', 'latest_transfer_time', 'pipeline', 'priority', 'relative_position', 'workspace')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    item_after = sgqlc.types.Field('PipelineIssue', graphql_name='itemAfter')
    item_before = sgqlc.types.Field('PipelineIssue', graphql_name='itemBefore')
    latest_transfer_time = sgqlc.types.Field(ISO8601DateTime, graphql_name='latestTransferTime')
    pipeline = sgqlc.types.Field(sgqlc.types.non_null('Pipeline'), graphql_name='pipeline')
    priority = sgqlc.types.Field('Priority', graphql_name='priority')
    relative_position = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='relativePosition')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class PipelineIssueConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineIssueEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineIssue))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PipelineIssueEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(PipelineIssue), graphql_name='node')


class PipelineIssueMove(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('moved_at', 'pipeline_issue', 'source_pipeline_id')
    moved_at = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='movedAt')
    pipeline_issue = sgqlc.types.Field(sgqlc.types.non_null(PipelineIssue), graphql_name='pipelineIssue')
    source_pipeline_id = sgqlc.types.Field(ID, graphql_name='sourcePipelineId')


class PipelineToPipelineAutomationConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineToPipelineAutomationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineToPipelineAutomation'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PipelineToPipelineAutomationEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PipelineToPipelineAutomation'), graphql_name='node')


class PriorityConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriorityEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Priority'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PriorityEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Priority'), graphql_name='node')


class ProjectAbilities(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('close_all_epics', 'scale_dates', 'shift_dates')
    close_all_epics = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closeAllEpics')
    scale_dates = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='scaleDates')
    shift_dates = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shiftDates')


class ProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Project'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='node')


class PullRequestReviewConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PullRequestReviewEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PullRequestReview'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='node')


class Query(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('issue_by_info', 'issue_connections', 'node', 'nodes', 'owner_by_gh_id', 'owner_by_login', 'preview_sprint_config', 'recently_viewed_workspaces', 'repositories_by_gh_id', 'search_closed_issues', 'search_issues', 'search_issues_by_pipeline', 'search_issues_by_zenhub_epics', 'triggered_pipeline_to_pipeline_automations', 'validate_workspace_name', 'viewer', 'workspace')
    issue_by_info = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issueByInfo', args=sgqlc.types.ArgDict((
        ('repository_gh_id', sgqlc.types.Arg(Int, graphql_name='repositoryGhId', default=None)),
        ('repository_id', sgqlc.types.Arg(ID, graphql_name='repositoryId', default=None)),
        ('issue_number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='issueNumber', default=None)),
))
    )
    issue_connections = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issueConnections', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspaceId', default=None)),
        ('issue_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds', default=None)),
))
    )
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Node)), graphql_name='nodes', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    owner_by_gh_id = sgqlc.types.Field(Owner, graphql_name='ownerByGhId', args=sgqlc.types.ArgDict((
        ('gh_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='ghId', default=None)),
))
    )
    owner_by_login = sgqlc.types.Field(Owner, graphql_name='ownerByLogin', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    preview_sprint_config = sgqlc.types.Field('SprintConfigPreview', graphql_name='previewSprintConfig', args=sgqlc.types.ArgDict((
        ('start_on', sgqlc.types.Arg(sgqlc.types.non_null(ISO8601Date), graphql_name='startOn', default=None)),
        ('end_on', sgqlc.types.Arg(sgqlc.types.non_null(ISO8601Date), graphql_name='endOn', default=None)),
        ('kind', sgqlc.types.Arg(SprintConfigKind, graphql_name='kind', default=None)),
        ('tz_identifier', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tzIdentifier', default=None)),
        ('workspace_id', sgqlc.types.Arg(ID, graphql_name='workspaceId', default=None)),
))
    )
    recently_viewed_workspaces = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceConnection'), graphql_name='recentlyViewedWorkspaces', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_gh_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryGhIds', default=None)),
        ('zenhub_organization_id', sgqlc.types.Arg(ID, graphql_name='zenhubOrganizationId', default=None)),
))
    )
    repositories_by_gh_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Repository'))), graphql_name='repositoriesByGhId', args=sgqlc.types.ArgDict((
        ('gh_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='ghIds', default=None)),
))
    )
    search_closed_issues = sgqlc.types.Field(IssueConnection, graphql_name='searchClosedIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspaceId', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filters', sgqlc.types.Arg(sgqlc.types.non_null(IssueSearchFiltersInput), graphql_name='filters', default=None)),
))
    )
    search_issues = sgqlc.types.Field(IssueConnection, graphql_name='searchIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspaceId', default=None)),
        ('filters', sgqlc.types.Arg(sgqlc.types.non_null(EpicAssignableIssueSearchFiltersInput), graphql_name='filters', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('include_closed', sgqlc.types.Arg(Boolean, graphql_name='includeClosed', default=None)),
))
    )
    search_issues_by_pipeline = sgqlc.types.Field(IssueConnection, graphql_name='searchIssuesByPipeline', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('pipeline_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='pipelineId', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order', sgqlc.types.Arg(IssueOrderInput, graphql_name='order', default=None)),
        ('filters', sgqlc.types.Arg(sgqlc.types.non_null(IssueSearchFiltersInput), graphql_name='filters', default=None)),
))
    )
    search_issues_by_zenhub_epics = sgqlc.types.Field(IssueConnection, graphql_name='searchIssuesByZenhubEpics', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(sgqlc.types.non_null(ZenhubEpicIssueSearchFiltersInput), graphql_name='filters', default=None)),
        ('zenhub_epic_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='zenhubEpicIds', default=None)),
))
    )
    triggered_pipeline_to_pipeline_automations = sgqlc.types.Field(sgqlc.types.non_null(PipelineToPipelineAutomationConnection), graphql_name='triggeredPipelineToPipelineAutomations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('issue', sgqlc.types.Arg(sgqlc.types.non_null(IssueInfoInput), graphql_name='issue', default=None)),
        ('pipeline_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='pipelineId', default=None)),
))
    )
    validate_workspace_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateWorkspaceName', args=sgqlc.types.ArgDict((
        ('zenhub_organization_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='zenhubOrganizationId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    viewer = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='viewer')
    workspace = sgqlc.types.Field('Workspace', graphql_name='workspace', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )


class ReleaseConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReleaseEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Release'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReleaseEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Release'), graphql_name='node')


class RemoveAssigneesFromIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'success_count')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')


class RemoveAssigneesFromZenhubEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class RemoveEpicFromProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class RemoveEpicFromRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class RemoveEstimateSetValuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'estimate_set')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    estimate_set = sgqlc.types.Field(sgqlc.types.non_null(EstimateSet), graphql_name='estimateSet')


class RemoveEstimationVotePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'estimation_vote')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    estimation_vote = sgqlc.types.Field(sgqlc.types.non_null('EstimationVote'), graphql_name='estimationVote')


class RemoveIssueInfoPrioritiesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineIssue))), graphql_name='pipelineIssues')


class RemoveIssuesFromEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Epic'))), graphql_name='epics')


class RemoveIssuesFromReleasesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'releases')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    releases = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Release'))), graphql_name='releases')


class RemoveIssuesFromSprintsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprints')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprints = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Sprint'))), graphql_name='sprints')


class RemoveIssuesFromZenhubEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class RemoveLabelsFromIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'labels', 'success_count')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Label'))), graphql_name='labels')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')


class RemoveMilestoneForIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'success_count')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')


class RemoveProjectFromRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project', 'project_deleted', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')
    project_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='projectDeleted')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class RemoveRepositoriesFromReleasePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'release')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    release = sgqlc.types.Field(sgqlc.types.non_null('Release'), graphql_name='release')


class RemoveUserFromZenhubOrganizationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')


class RemoveWorkspaceLabelFiltersPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_label_filters')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_label_filters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceLabelFilter'))), graphql_name='workspaceLabelFilters')


class RemoveZenhubAssigneesFromIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='issues')


class RemoveZenhubEpicFromProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class RemoveZenhubEpicFromRoadmapPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'roadmap', 'zenhub_epic', 'zenhub_epic_deleted')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')
    zenhub_epic_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='zenhubEpicDeleted')


class RemoveZenhubLabelsFromIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='issues')


class RemoveZenhubLabelsFromZenhubEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class RemoveZenhubRepositoryFromWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class RemoveZenhubUsersFromWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace', 'zenhub_users')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')
    zenhub_users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubUser'))), graphql_name='zenhubUsers')


class ReopenIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'failed_issues', 'github_errors', 'success_count')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    failed_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='failedIssues')
    github_errors = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='githubErrors')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')


class RepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Repository'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='node')


class RepositoryFavoriteConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryFavoriteEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryFavorite'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryFavoriteEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('RepositoryFavorite'), graphql_name='node')


class RepositoryGithubProjectImport(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('gh_project_id', 'gh_project_name', 'id', 'pipelines', 'repository')
    gh_project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ghProjectId')
    gh_project_name = sgqlc.types.Field(String, graphql_name='ghProjectName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pipelines = sgqlc.types.Field(sgqlc.types.non_null(PipelineConnection), graphql_name='pipelines', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class RepositoryImportResourceConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryImportResourceEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryImportResource'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryImportResourceEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('RepositoryImportResource'), graphql_name='node')


class RepositoryMatch(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('matched_repositories', 'workspace')
    matched_repositories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Repository'))), graphql_name='matchedRepositories')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class RepositoryPermission(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('admin', 'pull', 'push')
    admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='admin')
    pull = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pull')
    push = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='push')


class ReviewRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReviewRequestEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReviewRequest'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReviewRequestEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ReviewRequest'), graphql_name='node')


class RoadmapItemConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapItemEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapItem'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RoadmapItemDates(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('end_on', 'start_on')
    end_on = sgqlc.types.Field(ISO8601Date, graphql_name='endOn', args=sgqlc.types.ArgDict((
        ('roadmap_id', sgqlc.types.Arg(ID, graphql_name='roadmapId', default=None)),
))
    )
    start_on = sgqlc.types.Field(ISO8601Date, graphql_name='startOn', args=sgqlc.types.ArgDict((
        ('roadmap_id', sgqlc.types.Arg(ID, graphql_name='roadmapId', default=None)),
))
    )


class RoadmapItemEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RoadmapItem', graphql_name='node')


class SavedViewConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SavedViewEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SavedView'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SavedViewEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('SavedView'), graphql_name='node')


class ScopeChange(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('action', 'effective_at', 'estimate_value', 'issue')
    action = sgqlc.types.Field(sgqlc.types.non_null(BucketIssueHistoryAction), graphql_name='action')
    effective_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='effectiveAt')
    estimate_value = sgqlc.types.Field(Float, graphql_name='estimateValue')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class ScopeChangeConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ScopeChangeEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ScopeChange))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ScopeChangeEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(ScopeChange), graphql_name='node')


class SetEstimatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class SetEstimationVotePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'estimation_vote')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    estimation_vote = sgqlc.types.Field(sgqlc.types.non_null('EstimationVote'), graphql_name='estimationVote')


class SetFavoriteWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace_favorite')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace_favorite = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceFavorite'), graphql_name='workspaceFavorite')


class SetIssueInfoPrioritiesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineIssue))), graphql_name='pipelineIssues')


class SetMultipleEstimatesOnZenhubEpicsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epics')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='zenhubEpics')


class SetMultipleEstimatesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='issues')


class SetPipelineStagesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipelines')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipelines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Pipeline'))), graphql_name='pipelines')


class SetPriorityOnPipelineIssuesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineIssue))), graphql_name='pipelineIssues')


class SetPullRequestPipelinePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class SetWorkspaceViewedNowPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class SplitWorkspaceRepositoryPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'split_workspace', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    split_workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='splitWorkspace')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class SprintConfigMonthlyAttributes(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('end_day', 'period', 'start_day')
    end_day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endDay')
    period = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='period')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='startDay')


class SprintConfigPreview(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('period_in_weeks', 'sprints')
    period_in_weeks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='periodInWeeks')
    sprints = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Sprint'))), graphql_name='sprints')


class SprintConfigSettings(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('issues_from_pipeline', 'move_unfinished_issues')
    issues_from_pipeline = sgqlc.types.Field(sgqlc.types.non_null('SprintConfigSettingsIssuesFromPipeline'), graphql_name='issuesFromPipeline')
    move_unfinished_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='moveUnfinishedIssues')


class SprintConfigSettingsIssuesFromPipeline(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('enabled', 'pipeline_id', 'total_story_points')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    pipeline_id = sgqlc.types.Field(ID, graphql_name='pipelineId')
    total_story_points = sgqlc.types.Field(Float, graphql_name='totalStoryPoints')


class SprintConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Sprint'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SprintEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Sprint'), graphql_name='node')


class SprintIssueConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintIssueEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintIssue'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SprintIssueEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('SprintIssue'), graphql_name='node')


class SprintReviewFeatureConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintReviewFeatureEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintReviewFeature'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SprintReviewFeatureEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('SprintReviewFeature'), graphql_name='node')


class SprintReviewScheduleConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintReviewScheduleEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SprintReviewSchedule'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SprintReviewScheduleEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('SprintReviewSchedule'), graphql_name='node')


class TimelineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimelineItemEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimelineItem'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TimelineItemEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('TimelineItem'), graphql_name='node')


class Timestamps(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('created_at', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')


class Unassignable(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('assignee', 'issues')
    assignee = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='assignee')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='issues')


class UpdateCommentPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEpicDatesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')


class UpdateEpicIssuesByIssueInfosPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'epic', 'issues_added', 'issues_removed')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    epic = sgqlc.types.Field(sgqlc.types.non_null('Epic'), graphql_name='epic')
    issues_added = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Issue')), graphql_name='issuesAdded')
    issues_removed = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Issue')), graphql_name='issuesRemoved')


class UpdateIssuePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class UpdatePipelineAutomationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_automation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_automation = sgqlc.types.Field(sgqlc.types.non_null('PipelineAutomation'), graphql_name='pipelineAutomation')


class UpdatePipelineConfigurationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline_configuration')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline_configuration = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfiguration'), graphql_name='pipelineConfiguration')


class UpdatePipelinePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'pipeline')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pipeline = sgqlc.types.Field(sgqlc.types.non_null('Pipeline'), graphql_name='pipeline')


class UpdateProjectDatesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class UpdateProjectPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class UpdateProjectStatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class UpdateReleasePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'release')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    release = sgqlc.types.Field(sgqlc.types.non_null('Release'), graphql_name='release')


class UpdateRoadmapKeyDatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date', 'roadmap')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date = sgqlc.types.Field(sgqlc.types.non_null('KeyDate'), graphql_name='keyDate')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')


class UpdateSavedViewPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'saved_view')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    saved_view = sgqlc.types.Field(sgqlc.types.non_null('SavedView'), graphql_name='savedView')


class UpdateSprintConfigPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint_config')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint_config = sgqlc.types.Field(sgqlc.types.non_null('SprintConfig'), graphql_name='sprintConfig')


class UpdateSprintPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'sprint')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sprint = sgqlc.types.Field(sgqlc.types.non_null('Sprint'), graphql_name='sprint')


class UpdateUserPermissionsPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_org_user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_org_user = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUserAtOrganization'), graphql_name='zenhubOrgUser')


class UpdateWorkspacePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class UpdateWorkspaceZenhubUserRolePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'workspace')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class UpdateZenhubEpicDatesPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class UpdateZenhubEpicKeyDatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'key_date', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key_date = sgqlc.types.Field(sgqlc.types.non_null('KeyDate'), graphql_name='keyDate')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class UpdateZenhubEpicPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class UpdateZenhubEpicStatePayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_epic')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_epic = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='zenhubEpic')


class UpdateZenhubOrganizationPayload(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('client_mutation_id', 'zenhub_organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')


class UserConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')


class VelocityDiff(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('difference', 'sprints_count', 'velocity')
    difference = sgqlc.types.Field(Float, graphql_name='difference')
    sprints_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sprintsCount')
    velocity = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='velocity')


class ViewerPermission(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('viewer_permission',)
    viewer_permission = sgqlc.types.Field(sgqlc.types.non_null(PermissionLevel), graphql_name='viewerPermission')


class WipLimit(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('block_pipeline', 'id', 'limit_value')
    block_pipeline = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='blockPipeline')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    limit_value = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='limitValue')


class WipLimitConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WipLimitEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WipLimit))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WipLimitEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(WipLimit), graphql_name='node')


class WorkspaceConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Workspace'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkspaceEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='node')


class WorkspaceFavoriteConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceFavoriteEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceFavorite'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkspaceFavoriteEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceFavorite'), graphql_name='node')


class WorkspaceLabelFilter(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'label_name', 'workspace', 'zenhub_label')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='labelName')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')
    zenhub_label = sgqlc.types.Field('ZenhubLabel', graphql_name='zenhubLabel')


class WorkspaceLabelFilterConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceLabelFilterEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkspaceLabelFilter))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkspaceLabelFilterEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceLabelFilter), graphql_name='node')


class WorkspaceMatch(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('workspace',)
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class WorkspaceRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceRepositoryEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceRepository'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkspaceRepositoryEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceRepository'), graphql_name='node')


class WorkspaceSearchMatchConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceSearchMatchEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceSearchMatch'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkspaceSearchMatchEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('WorkspaceSearchMatch', graphql_name='node')


class ZenhubEpicConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpicEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubEpic'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ZenhubEpicEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ZenhubEpic'), graphql_name='node')


class ZenhubEpicIssueProgress(sgqlc.types.Interface):
    __schema__ = zenhub_schema
    __field_names__ = ('zenhub_issue_count_progress', 'zenhub_issue_estimate_progress')
    zenhub_issue_count_progress = sgqlc.types.Field(IssueCountProgress, graphql_name='zenhubIssueCountProgress')
    zenhub_issue_estimate_progress = sgqlc.types.Field(IssueEstimateProgress, graphql_name='zenhubIssueEstimateProgress')


class ZenhubLabelConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubLabelEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubLabel'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ZenhubLabelEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ZenhubLabel'), graphql_name='node')


class ZenhubOrganizationConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubOrganizationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubOrganization'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ZenhubOrganizationEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='node')


class ZenhubUserAtOrganizationConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubUserAtOrganizationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubUserAtOrganization'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ZenhubUserAtOrganizationEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUserAtOrganization'), graphql_name='node')


class ZenhubUserConnection(sgqlc.types.relay.Connection):
    __schema__ = zenhub_schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubUserEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZenhubUser'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ZenhubUserEdge(sgqlc.types.Type):
    __schema__ = zenhub_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='node')


class Blockage(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('blocked', 'blocking')
    blocked = sgqlc.types.Field(sgqlc.types.non_null('IssueDependencyItem'), graphql_name='blocked')
    blocking = sgqlc.types.Field(sgqlc.types.non_null('IssueDependencyItem'), graphql_name='blocking')


class Bot(sgqlc.types.Type, Owner, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ()


class Comment(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('author', 'body', 'commentable', 'editor', 'html_body', 'last_edited_at')
    author = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='author')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    commentable = sgqlc.types.Field(sgqlc.types.non_null('Commentable'), graphql_name='commentable')
    editor = sgqlc.types.Field('ZenhubUser', graphql_name='editor')
    html_body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='htmlBody')
    last_edited_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='lastEditedAt')


class Epic(sgqlc.types.Type, IssueProgress, Node, RoadmapItemDates, Timestamps, ViewerPermission):
    __schema__ = zenhub_schema
    __field_names__ = ('child_issues', 'issue', 'project')
    child_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='childIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueFiltersInput, graphql_name='filters', default=None)),
))
    )
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    project = sgqlc.types.Field('Project', graphql_name='project')


class Estimate(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class EstimationVote(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'issue', 'value', 'voter')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    value = sgqlc.types.Field(Float, graphql_name='value')
    voter = sgqlc.types.Field(sgqlc.types.non_null('ZenhubUser'), graphql_name='voter')


class Issue(sgqlc.types.Type, ActivityFeedField, GithubTimestamps, Node, Timestamps, ViewerPermission):
    __schema__ = zenhub_schema
    __field_names__ = ('assignees', 'blocked_issues', 'blocked_items', 'blocking_issues', 'blocking_items', 'body', 'closed_at', 'comments', 'connected_prs', 'connections', 'estimate', 'estimation_votes', 'gh_id', 'gh_node_id', 'html_body', 'html_url', 'labels', 'milestone', 'number', 'parent_zenhub_epics', 'pipeline_issue', 'pipeline_issues', 'pull_request', 'pull_request_object', 'pull_request_reviews', 'releases', 'repository', 'review_requests', 'sprints', 'state', 'timeline_items', 'title', 'type', 'user', 'zenhub_assignees', 'zenhub_labels')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    blocked_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='blockedIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueFiltersInput, graphql_name='filters', default=None)),
))
    )
    blocked_items = sgqlc.types.Field(sgqlc.types.non_null(IssueDependencyItemConnection), graphql_name='blockedItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueDependencyItemFiltersInput, graphql_name='filters', default=None)),
))
    )
    blocking_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='blockingIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueFiltersInput, graphql_name='filters', default=None)),
))
    )
    blocking_items = sgqlc.types.Field(sgqlc.types.non_null(IssueDependencyItemConnection), graphql_name='blockingItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueDependencyItemFiltersInput, graphql_name='filters', default=None)),
))
    )
    body = sgqlc.types.Field(String, graphql_name='body')
    closed_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='closedAt')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    connected_prs = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='connectedPrs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    connections = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='connections', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    estimate = sgqlc.types.Field(Estimate, graphql_name='estimate')
    estimation_votes = sgqlc.types.Field(sgqlc.types.non_null(EstimationVoteConnection), graphql_name='estimationVotes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    gh_id = sgqlc.types.Field(Int, graphql_name='ghId')
    gh_node_id = sgqlc.types.Field(ID, graphql_name='ghNodeId')
    html_body = sgqlc.types.Field(String, graphql_name='htmlBody')
    html_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='htmlUrl')
    labels = sgqlc.types.Field(sgqlc.types.non_null(LabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    milestone = sgqlc.types.Field('Milestone', graphql_name='milestone')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    parent_zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(ZenhubEpicConnection), graphql_name='parentZenhubEpics', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pipeline_issue = sgqlc.types.Field(PipelineIssue, graphql_name='pipelineIssue', args=sgqlc.types.ArgDict((
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspaceId', default=None)),
))
    )
    pipeline_issues = sgqlc.types.Field(sgqlc.types.non_null(PipelineIssueConnection), graphql_name='pipelineIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pullRequest')
    pull_request_object = sgqlc.types.Field('PullRequest', graphql_name='pullRequestObject')
    pull_request_reviews = sgqlc.types.Field(PullRequestReviewConnection, graphql_name='pullRequestReviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    releases = sgqlc.types.Field(sgqlc.types.non_null(ReleaseConnection), graphql_name='releases', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    review_requests = sgqlc.types.Field(ReviewRequestConnection, graphql_name='reviewRequests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    sprints = sgqlc.types.Field(sgqlc.types.non_null(SprintConnection), graphql_name='sprints', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('workspace_id', sgqlc.types.Arg(ID, graphql_name='workspaceId', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(IssueState), graphql_name='state')
    timeline_items = sgqlc.types.Field(sgqlc.types.non_null(TimelineItemConnection), graphql_name='timelineItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(IssueType), graphql_name='type')
    user = sgqlc.types.Field(sgqlc.types.non_null(Owner), graphql_name='user')
    zenhub_assignees = sgqlc.types.Field(sgqlc.types.non_null(ZenhubUserConnection), graphql_name='zenhubAssignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    zenhub_labels = sgqlc.types.Field(sgqlc.types.non_null(ZenhubLabelConnection), graphql_name='zenhubLabels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class IssueDependency(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('blocked_issue', 'blocking_issue')
    blocked_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='blockedIssue')
    blocking_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='blockingIssue')


class KeyDate(sgqlc.types.Type, Node):
    __schema__ = zenhub_schema
    __field_names__ = ('color', 'date', 'description')
    color = sgqlc.types.Field(String, graphql_name='color')
    date = sgqlc.types.Field(sgqlc.types.non_null(ISO8601Date), graphql_name='date')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class Label(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('color', 'description', 'gh_id', 'gh_node_id', 'id', 'issues', 'name', 'repository')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    gh_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='ghId')
    gh_node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ghNodeId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class Mannequin(sgqlc.types.Type, Owner, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ()


class Milestone(sgqlc.types.Type, GithubTimestamps, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ()


class NoOwner(sgqlc.types.Type, Owner):
    __schema__ = zenhub_schema
    __field_names__ = ()


class Organization(sgqlc.types.Type, Owner, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('zenhub_organization',)
    zenhub_organization = sgqlc.types.Field('ZenhubOrganization', graphql_name='zenhubOrganization')


class Pipeline(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('description', 'has_estimated_issues', 'is_default_prpipeline', 'issues', 'item_before', 'name', 'pipeline_configuration', 'pipeline_to_pipeline_automation_destinations', 'pipeline_to_pipeline_automation_sources', 'stage', 'workspace')
    description = sgqlc.types.Field(String, graphql_name='description')
    has_estimated_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasEstimatedIssues')
    is_default_prpipeline = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefaultPRPipeline')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_id', sgqlc.types.Arg(ID, graphql_name='repositoryId', default=None)),
        ('state', sgqlc.types.Arg(IssueState, graphql_name='state', default=None)),
))
    )
    item_before = sgqlc.types.Field('Pipeline', graphql_name='itemBefore')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pipeline_configuration = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfiguration'), graphql_name='pipelineConfiguration')
    pipeline_to_pipeline_automation_destinations = sgqlc.types.Field(sgqlc.types.non_null(PipelineToPipelineAutomationConnection), graphql_name='pipelineToPipelineAutomationDestinations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pipeline_to_pipeline_automation_sources = sgqlc.types.Field(sgqlc.types.non_null(PipelineToPipelineAutomationConnection), graphql_name='pipelineToPipelineAutomationSources', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    stage = sgqlc.types.Field(PipelineStage, graphql_name='stage')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class PipelineAutomation(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('element_details', 'id')
    element_details = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='elementDetails')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class PipelineConfiguration(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'pipeline_automations', 'stale_interval', 'stale_issues', 'wip_limits')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pipeline_automations = sgqlc.types.Field(sgqlc.types.non_null(PipelineAutomationConnection), graphql_name='pipelineAutomations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    stale_interval = sgqlc.types.Field(Int, graphql_name='staleInterval')
    stale_issues = sgqlc.types.Field(Boolean, graphql_name='staleIssues')
    wip_limits = sgqlc.types.Field(sgqlc.types.non_null(WipLimitConnection), graphql_name='wipLimits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class PipelineToPipelineAutomation(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('destination_pipeline', 'source_pipeline')
    destination_pipeline = sgqlc.types.Field(sgqlc.types.non_null(Pipeline), graphql_name='destinationPipeline')
    source_pipeline = sgqlc.types.Field(sgqlc.types.non_null(Pipeline), graphql_name='sourcePipeline')


class Priority(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('color', 'description', 'id', 'name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Project(sgqlc.types.Type, IssueProgress, Node, RoadmapItemDates, Timestamps, ViewerPermission, ZenhubEpicIssueProgress):
    __schema__ = zenhub_schema
    __field_names__ = ('closed_at', 'creator', 'description', 'html_body', 'name', 'state', 'viewer_abilities', 'zenhub_epics')
    closed_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='closedAt')
    creator = sgqlc.types.Field('ZenhubUser', graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    html_body = sgqlc.types.Field(String, graphql_name='htmlBody')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    state = sgqlc.types.Field(sgqlc.types.non_null(ProjectState), graphql_name='state')
    viewer_abilities = sgqlc.types.Field(sgqlc.types.non_null(ProjectAbilities), graphql_name='viewerAbilities')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(ZenhubEpicConnection), graphql_name='zenhubEpics', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(ZenhubEpicStateFilterInput, graphql_name='state', default=None)),
        ('order', sgqlc.types.Arg(RoadmapItemOrderInput, graphql_name='order', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )


class PullRequest(sgqlc.types.Type, GithubTimestamps, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('draft', 'id', 'issue', 'state')
    draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='draft')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestState), graphql_name='state')


class PullRequestReview(sgqlc.types.Type, GithubTimestamps, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('gh_id', 'gh_node_id', 'id', 'state', 'submitted_at', 'user')
    gh_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ghId')
    gh_node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ghNodeId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewState), graphql_name='state')
    submitted_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='submittedAt')
    user = sgqlc.types.Field(Owner, graphql_name='user')


class Release(sgqlc.types.Type, Node, Timestamps, ViewerPermission):
    __schema__ = zenhub_schema
    __field_names__ = ('closed_at', 'description', 'end_on', 'issues', 'issues_count', 'repositories', 'start_on', 'state', 'title')
    closed_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='closedAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    end_on = sgqlc.types.Field(ISO8601Date, graphql_name='endOn')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    issues_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issuesCount')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    start_on = sgqlc.types.Field(ISO8601Date, graphql_name='startOn')
    state = sgqlc.types.Field(sgqlc.types.non_null(ReleaseState), graphql_name='state')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class Repository(sgqlc.types.Type, GithubTimestamps, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('assignable_users', 'description', 'estimate_set', 'gh_id', 'gh_node_id', 'import_', 'is_archived', 'is_favorite', 'is_private', 'issue_templates', 'issues', 'labels', 'milestones', 'name', 'owner', 'owner_name', 'permissions', 'releases', 'type', 'workspace', 'workspaces_connection')
    assignable_users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignableUsers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    estimate_set = sgqlc.types.Field(sgqlc.types.non_null(EstimateSet), graphql_name='estimateSet')
    gh_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ghId')
    gh_node_id = sgqlc.types.Field(ID, graphql_name='ghNodeId')
    import_ = sgqlc.types.Field(sgqlc.types.non_null('RepositoryImport'), graphql_name='import')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_favorite = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFavorite')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    issue_templates = sgqlc.types.Field(sgqlc.types.non_null(IssueTemplateConnection), graphql_name='issueTemplates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(LabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    milestones = sgqlc.types.Field(sgqlc.types.non_null(MilestoneConnection), graphql_name='milestones', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner = sgqlc.types.Field(sgqlc.types.non_null(Owner), graphql_name='owner')
    owner_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ownerName')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permissions')
    releases = sgqlc.types.Field(sgqlc.types.non_null(ReleaseConnection), graphql_name='releases', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    type = sgqlc.types.Field(sgqlc.types.non_null(RepositoryType), graphql_name='type')
    workspace = sgqlc.types.Field('Workspace', graphql_name='workspace')
    workspaces_connection = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceConnection), graphql_name='workspacesConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class RepositoryFavorite(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'repository')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')


class RepositoryImport(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'resources', 'state')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    resources = sgqlc.types.Field(sgqlc.types.non_null(RepositoryImportResourceConnection), graphql_name='resources', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(RepositoryImportState), graphql_name='state')


class RepositoryImportResource(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('completed_at', 'completed_pages', 'id', 'kind', 'started_at', 'state', 'total_pages')
    completed_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='completedAt')
    completed_pages = sgqlc.types.Field(Int, graphql_name='completedPages')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    kind = sgqlc.types.Field(sgqlc.types.non_null(RepositoryImportResourceKind), graphql_name='kind')
    started_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='startedAt')
    state = sgqlc.types.Field(sgqlc.types.non_null(RepositoryImportResourceState), graphql_name='state')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')


class ReviewRequest(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('gh_id', 'gh_node_id', 'id', 'reviewer')
    gh_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ghId')
    gh_node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ghNodeId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reviewer = sgqlc.types.Field('Reviewer', graphql_name='reviewer')


class Roadmap(sgqlc.types.Type, Node, Timestamps, ViewerPermission):
    __schema__ = zenhub_schema
    __field_names__ = ('items', 'key_dates', 'workspace')
    items = sgqlc.types.Field(sgqlc.types.non_null(RoadmapItemConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order', sgqlc.types.Arg(RoadmapItemOrderInput, graphql_name='order', default=None)),
        ('state', sgqlc.types.Arg(RoadmapItemStateFilterInput, graphql_name='state', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('start_on', sgqlc.types.Arg(ISO8601Date, graphql_name='startOn', default=None)),
        ('end_on', sgqlc.types.Arg(ISO8601Date, graphql_name='endOn', default=None)),
))
    )
    key_dates = sgqlc.types.Field(KeyDateConnection, graphql_name='keyDates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('start_date', sgqlc.types.Arg(ISO8601Date, graphql_name='startDate', default=None)),
        ('end_date', sgqlc.types.Arg(ISO8601Date, graphql_name='endDate', default=None)),
))
    )
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class SavedView(sgqlc.types.Type, Node):
    __schema__ = zenhub_schema
    __field_names__ = ()


class Sprint(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('closed_issues_count', 'completed_points', 'description', 'end_at', 'generated_name', 'issues', 'name', 'persisted', 'scope_change', 'sprint_issues', 'sprint_review', 'start_at', 'state', 'total_points', 'workspace')
    closed_issues_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='closedIssuesCount')
    completed_points = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='completedPoints')
    description = sgqlc.types.Field(String, graphql_name='description')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='endAt')
    generated_name = sgqlc.types.Field(String, graphql_name='generatedName')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    persisted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='persisted')
    scope_change = sgqlc.types.Field(sgqlc.types.non_null(ScopeChangeConnection), graphql_name='scopeChange', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    sprint_issues = sgqlc.types.Field(sgqlc.types.non_null(SprintIssueConnection), graphql_name='sprintIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('label_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds', default=None)),
))
    )
    sprint_review = sgqlc.types.Field('SprintReview', graphql_name='sprintReview')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='startAt')
    state = sgqlc.types.Field(sgqlc.types.non_null(SprintState), graphql_name='state')
    total_points = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalPoints')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class SprintConfig(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('end_day', 'kind', 'monthly_attributes', 'name', 'period', 'settings', 'start_day', 'tz_identifier', 'workspace')
    end_day = sgqlc.types.Field(sgqlc.types.non_null(SprintConfigDayOfTheWeek), graphql_name='endDay')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SprintConfigKind), graphql_name='kind')
    monthly_attributes = sgqlc.types.Field(SprintConfigMonthlyAttributes, graphql_name='monthlyAttributes')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    period = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='period')
    settings = sgqlc.types.Field(sgqlc.types.non_null(SprintConfigSettings), graphql_name='settings')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(SprintConfigDayOfTheWeek), graphql_name='startDay')
    tz_identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tzIdentifier')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class SprintIssue(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('issue', 'sprint')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    sprint = sgqlc.types.Field(sgqlc.types.non_null(Sprint), graphql_name='sprint')


class SprintReview(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('body', 'html_body', 'initiated_by', 'issues_closed_after_sprint_review', 'language', 'last_generated_at', 'manually_edited', 'sprint', 'sprint_review_features', 'sprint_review_schedules', 'state', 'title')
    body = sgqlc.types.Field(String, graphql_name='body')
    html_body = sgqlc.types.Field(String, graphql_name='htmlBody')
    initiated_by = sgqlc.types.Field('ZenhubUser', graphql_name='initiatedBy')
    issues_closed_after_sprint_review = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issuesClosedAfterSprintReview', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    language = sgqlc.types.Field(String, graphql_name='language')
    last_generated_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='lastGeneratedAt')
    manually_edited = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='manuallyEdited')
    sprint = sgqlc.types.Field(sgqlc.types.non_null(Sprint), graphql_name='sprint')
    sprint_review_features = sgqlc.types.Field(sgqlc.types.non_null(SprintReviewFeatureConnection), graphql_name='sprintReviewFeatures', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    sprint_review_schedules = sgqlc.types.Field(sgqlc.types.non_null(SprintReviewScheduleConnection), graphql_name='sprintReviewSchedules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(SprintReviewState), graphql_name='state')
    title = sgqlc.types.Field(String, graphql_name='title')


class SprintReviewFeature(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('ai_generated_issues', 'manually_added_issues', 'title')
    ai_generated_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='aiGeneratedIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    manually_added_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='manuallyAddedIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class SprintReviewSchedule(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('completed_at', 'start_at', 'title')
    completed_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='completedAt')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='startAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class TimelineItem(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('data', 'id', 'key')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class User(sgqlc.types.Type, Owner, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('name', 'zenhub_user')
    name = sgqlc.types.Field(String, graphql_name='name')
    zenhub_user = sgqlc.types.Field('ZenhubUser', graphql_name='zenhubUser')


class Workspace(sgqlc.types.Type, Timestamps, ViewerPermission):
    __schema__ = zenhub_schema
    __field_names__ = ('active_sprint', 'are_uploaded_files_private', 'assignees', 'assume_estimates', 'authors', 'average_sprint_velocity', 'average_sprint_velocity_with_diff', 'closed_pipeline', 'creator', 'default_repository', 'description', 'display_name', 'has_estimated_issues', 'id', 'import_state', 'is_deletable', 'is_editable', 'is_favorite', 'issue_assignee_options', 'issue_author_options', 'issue_dependencies', 'issue_flow_stats', 'issue_label_options', 'issues', 'label_filters', 'name', 'pipeline_to_pipeline_automations', 'pipelines_connection', 'previous_sprint', 'priorities_connection', 'private', 'projects', 'related_workspaces', 'releases', 'repositories_connection', 'repository_github_project_import', 'roadmap', 'saved_views', 'shared_zenhub_repositories', 'sprint_config', 'sprints', 'upcoming_sprint', 'workspace_repositories', 'zenhub_epics', 'zenhub_issue_by_number', 'zenhub_labels', 'zenhub_organization', 'zenhub_owner', 'zenhub_repository', 'zenhub_users')
    active_sprint = sgqlc.types.Field(Sprint, graphql_name='activeSprint')
    are_uploaded_files_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='areUploadedFilesPrivate')
    assignees = sgqlc.types.Field(UserConnection, graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('login', sgqlc.types.Arg(StringInput, graphql_name='login', default=None)),
        ('repository_gh_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='repositoryGhIds', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    assume_estimates = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='assumeEstimates')
    authors = sgqlc.types.Field(UserConnection, graphql_name='authors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('login', sgqlc.types.Arg(StringInput, graphql_name='login', default=None)),
        ('repository_gh_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='repositoryGhIds', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    average_sprint_velocity = sgqlc.types.Field(Float, graphql_name='averageSprintVelocity')
    average_sprint_velocity_with_diff = sgqlc.types.Field(VelocityDiff, graphql_name='averageSprintVelocityWithDiff', args=sgqlc.types.ArgDict((
        ('skip_diff', sgqlc.types.Arg(Boolean, graphql_name='skipDiff', default=None)),
))
    )
    closed_pipeline = sgqlc.types.Field(sgqlc.types.non_null(Pipeline), graphql_name='closedPipeline')
    creator = sgqlc.types.Field('ZenhubUser', graphql_name='creator')
    default_repository = sgqlc.types.Field(Repository, graphql_name='defaultRepository')
    description = sgqlc.types.Field(String, graphql_name='description')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    has_estimated_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasEstimatedIssues')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    import_state = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceImportState), graphql_name='importState')
    is_deletable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeletable')
    is_editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEditable')
    is_favorite = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFavorite')
    issue_assignee_options = sgqlc.types.Field(IssueUserOptionConnection, graphql_name='issueAssigneeOptions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('ids', sgqlc.types.Arg(StringInput, graphql_name='ids', default=None)),
        ('logins', sgqlc.types.Arg(StringInput, graphql_name='logins', default=None)),
        ('in_use', sgqlc.types.Arg(Boolean, graphql_name='inUse', default=None)),
))
    )
    issue_author_options = sgqlc.types.Field(IssueUserOptionConnection, graphql_name='issueAuthorOptions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('ids', sgqlc.types.Arg(StringInput, graphql_name='ids', default=None)),
        ('logins', sgqlc.types.Arg(StringInput, graphql_name='logins', default=None)),
))
    )
    issue_dependencies = sgqlc.types.Field(IssueDependencyConnection, graphql_name='issueDependencies', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds', default=None)),
))
    )
    issue_flow_stats = sgqlc.types.Field(IssueFlowStats, graphql_name='issueFlowStats', args=sgqlc.types.ArgDict((
        ('days_in_cycle', sgqlc.types.Arg(Int, graphql_name='daysInCycle', default=None)),
))
    )
    issue_label_options = sgqlc.types.Field(IssueLabelOptionConnection, graphql_name='issueLabelOptions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('name', sgqlc.types.Arg(StringInput, graphql_name='name', default=None)),
        ('repository_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('in_use', sgqlc.types.Arg(Boolean, graphql_name='inUse', default=None)),
        ('include_workspace_labels', sgqlc.types.Arg(Boolean, graphql_name='includeWorkspaceLabels', default=None)),
))
    )
    issues = sgqlc.types.Field(IssueConnection, graphql_name='issues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrderInput, graphql_name='orderBy', default=None)),
))
    )
    label_filters = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceLabelFilterConnection), graphql_name='labelFilters', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    pipeline_to_pipeline_automations = sgqlc.types.Field(sgqlc.types.non_null(PipelineToPipelineAutomationConnection), graphql_name='pipelineToPipelineAutomations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pipelines_connection = sgqlc.types.Field(sgqlc.types.non_null(PipelineConnection), graphql_name='pipelinesConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    previous_sprint = sgqlc.types.Field(Sprint, graphql_name='previousSprint')
    priorities_connection = sgqlc.types.Field(sgqlc.types.non_null(PriorityConnection), graphql_name='prioritiesConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='private')
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    related_workspaces = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceConnection), graphql_name='relatedWorkspaces', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    releases = sgqlc.types.Field(sgqlc.types.non_null(ReleaseConnection), graphql_name='releases', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('repository_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds', default=None)),
        ('state', sgqlc.types.Arg(ReleaseStateInput, graphql_name='state', default=None)),
))
    )
    repositories_connection = sgqlc.types.Field(RepositoryConnection, graphql_name='repositoriesConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository_github_project_import = sgqlc.types.Field(RepositoryGithubProjectImport, graphql_name='repositoryGithubProjectImport')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null(Roadmap), graphql_name='roadmap')
    saved_views = sgqlc.types.Field(sgqlc.types.non_null(SavedViewConnection), graphql_name='savedViews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    shared_zenhub_repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='sharedZenhubRepositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    sprint_config = sgqlc.types.Field(SprintConfig, graphql_name='sprintConfig')
    sprints = sgqlc.types.Field(sgqlc.types.non_null(SprintConnection), graphql_name='sprints', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filters', sgqlc.types.Arg(SprintFiltersInput, graphql_name='filters', default=None)),
        ('order_by', sgqlc.types.Arg(SprintOrderInput, graphql_name='orderBy', default=None)),
))
    )
    upcoming_sprint = sgqlc.types.Field(Sprint, graphql_name='upcomingSprint')
    workspace_repositories = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceRepositoryConnection), graphql_name='workspaceRepositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    zenhub_epics = sgqlc.types.Field(ZenhubEpicConnection, graphql_name='zenhubEpics', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filters', sgqlc.types.Arg(ZenhubEpicFiltersInput, graphql_name='filters', default=None)),
        ('order_by', sgqlc.types.Arg(ZenhubEpicOrderInput, graphql_name='orderBy', default=None)),
))
    )
    zenhub_issue_by_number = sgqlc.types.Field(Issue, graphql_name='zenhubIssueByNumber', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    zenhub_labels = sgqlc.types.Field(ZenhubLabelConnection, graphql_name='zenhubLabels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')
    zenhub_owner = sgqlc.types.Field('ZenhubIdentity', graphql_name='zenhubOwner')
    zenhub_repository = sgqlc.types.Field(Repository, graphql_name='zenhubRepository')
    zenhub_users = sgqlc.types.Field(sgqlc.types.non_null(ZenhubUserConnection), graphql_name='zenhubUsers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filters', sgqlc.types.Arg(ZenhubUsersFiltersInput, graphql_name='filters', default=None)),
))
    )


class WorkspaceFavorite(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'workspace')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    workspace = sgqlc.types.Field(sgqlc.types.non_null(Workspace), graphql_name='workspace')


class WorkspaceRepository(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'read_mode_enabled', 'repository', 'workspace')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    read_mode_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readModeEnabled')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    workspace = sgqlc.types.Field(sgqlc.types.non_null(Workspace), graphql_name='workspace')


class WorkspaceSharedZenhubRepository(sgqlc.types.Type, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('id', 'workspace', 'zenhub_repository')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    workspace = sgqlc.types.Field(sgqlc.types.non_null(Workspace), graphql_name='workspace')
    zenhub_repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='zenhubRepository')


class ZenhubEpic(sgqlc.types.Type, ActivityFeedField, Node, RoadmapItemDates, Timestamps, ViewerPermission, ZenhubEpicIssueProgress):
    __schema__ = zenhub_schema
    __field_names__ = ('assignees', 'blocked_items', 'blocking_items', 'body', 'child_issues', 'comments', 'creator', 'estimate', 'html_body', 'key_dates', 'labels', 'old_issue', 'project', 'related_items', 'state', 'title', 'zenhub_organization')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(ZenhubUserConnection), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    blocked_items = sgqlc.types.Field(sgqlc.types.non_null(IssueDependencyItemConnection), graphql_name='blockedItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueDependencyItemFiltersInput, graphql_name='filters', default=None)),
))
    )
    blocking_items = sgqlc.types.Field(sgqlc.types.non_null(IssueDependencyItemConnection), graphql_name='blockingItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueDependencyItemFiltersInput, graphql_name='filters', default=None)),
))
    )
    body = sgqlc.types.Field(String, graphql_name='body')
    child_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='childIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspaceId', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    creator = sgqlc.types.Field('ZenhubUser', graphql_name='creator')
    estimate = sgqlc.types.Field(Estimate, graphql_name='estimate')
    html_body = sgqlc.types.Field(String, graphql_name='htmlBody')
    key_dates = sgqlc.types.Field(sgqlc.types.non_null(KeyDateConnection), graphql_name='keyDates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(LabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    old_issue = sgqlc.types.Field(Issue, graphql_name='oldIssue')
    project = sgqlc.types.Field(Project, graphql_name='project')
    related_items = sgqlc.types.Field(sgqlc.types.non_null(IssueDependencyItemConnection), graphql_name='relatedItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filters', sgqlc.types.Arg(IssueDependencyItemFiltersInput, graphql_name='filters', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(ZenhubEpicState), graphql_name='state')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')


class ZenhubLabel(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('color', 'description', 'name', 'zenhub_epics', 'zenhub_organization')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    zenhub_epics = sgqlc.types.Field(sgqlc.types.non_null(ZenhubEpicConnection), graphql_name='zenhubEpics', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    zenhub_organization = sgqlc.types.Field(sgqlc.types.non_null('ZenhubOrganization'), graphql_name='zenhubOrganization')


class ZenhubOrganization(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('creator', 'github_organization', 'name', 'roadmap_items', 'workspaces', 'zenhub_labels', 'zenhub_users_at_organization')
    creator = sgqlc.types.Field('ZenhubUser', graphql_name='creator')
    github_organization = sgqlc.types.Field(Organization, graphql_name='githubOrganization')
    name = sgqlc.types.Field(String, graphql_name='name')
    roadmap_items = sgqlc.types.Field(sgqlc.types.non_null(RoadmapItemConnection), graphql_name='roadmapItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(RoadmapItemStateFilterInput, graphql_name='state', default=None)),
        ('order', sgqlc.types.Arg(RoadmapItemOrderInput, graphql_name='order', default={'field': 'end_on', 'direction': 'ASC'})),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('start_on', sgqlc.types.Arg(ISO8601Date, graphql_name='startOn', default=None)),
        ('end_on', sgqlc.types.Arg(ISO8601Date, graphql_name='endOn', default=None)),
))
    )
    workspaces = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceConnection), graphql_name='workspaces', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(WorkspaceOrderInput, graphql_name='orderBy', default=None)),
))
    )
    zenhub_labels = sgqlc.types.Field(sgqlc.types.non_null(ZenhubLabelConnection), graphql_name='zenhubLabels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    zenhub_users_at_organization = sgqlc.types.Field(ZenhubUserAtOrganizationConnection, graphql_name='zenhubUsersAtOrganization', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('platform_only', sgqlc.types.Arg(Boolean, graphql_name='platformOnly', default=None)),
        ('emails', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='emails', default=None)),
        ('order', sgqlc.types.Arg(ZenhubUserOrderInput, graphql_name='order', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('seated', sgqlc.types.Arg(Boolean, graphql_name='seated', default=None)),
        ('seat_request_pending', sgqlc.types.Arg(Boolean, graphql_name='seatRequestPending', default=None)),
        ('role', sgqlc.types.Arg(Roles, graphql_name='role', default=None)),
        ('include_external', sgqlc.types.Arg(Boolean, graphql_name='includeExternal', default=None)),
))
    )


class ZenhubOrganizationLimited(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class ZenhubUser(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('contact_email', 'email', 'estimation_groups', 'external_only', 'github_user', 'image_url', 'name', 'search_workspaces', 'workspace_favorites', 'zenhub_organizations')
    contact_email = sgqlc.types.Field(String, graphql_name='contactEmail')
    email = sgqlc.types.Field(String, graphql_name='email')
    estimation_groups = sgqlc.types.Field(sgqlc.types.non_null(EstimationGroupConnection), graphql_name='estimationGroups', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspaceId', default=None)),
))
    )
    external_only = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='externalOnly')
    github_user = sgqlc.types.Field(User, graphql_name='githubUser')
    image_url = sgqlc.types.Field(String, graphql_name='imageUrl')
    name = sgqlc.types.Field(String, graphql_name='name')
    search_workspaces = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceConnection), graphql_name='searchWorkspaces', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
))
    )
    workspace_favorites = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceFavoriteConnection), graphql_name='workspaceFavorites', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    zenhub_organizations = sgqlc.types.Field(sgqlc.types.non_null(ZenhubOrganizationConnection), graphql_name='zenhubOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )


class ZenhubUserAtOrganization(sgqlc.types.Type, Node, Timestamps):
    __schema__ = zenhub_schema
    __field_names__ = ('contact_email', 'email', 'estimation_groups', 'external_only', 'github_user', 'image_url', 'name', 'role', 'search_workspaces', 'seat_requested_at', 'seated', 'workspace_favorites', 'zenhub_organizations')
    contact_email = sgqlc.types.Field(String, graphql_name='contactEmail')
    email = sgqlc.types.Field(String, graphql_name='email')
    estimation_groups = sgqlc.types.Field(sgqlc.types.non_null(EstimationGroupConnection), graphql_name='estimationGroups', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspaceId', default=None)),
))
    )
    external_only = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='externalOnly')
    github_user = sgqlc.types.Field(User, graphql_name='githubUser')
    image_url = sgqlc.types.Field(String, graphql_name='imageUrl')
    name = sgqlc.types.Field(String, graphql_name='name')
    role = sgqlc.types.Field(Roles, graphql_name='role')
    search_workspaces = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceConnection), graphql_name='searchWorkspaces', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
))
    )
    seat_requested_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='seatRequestedAt')
    seated = sgqlc.types.Field(Boolean, graphql_name='seated')
    workspace_favorites = sgqlc.types.Field(sgqlc.types.non_null(WorkspaceFavoriteConnection), graphql_name='workspaceFavorites', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    zenhub_organizations = sgqlc.types.Field(sgqlc.types.non_null(ZenhubOrganizationConnection), graphql_name='zenhubOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )



########################################################################
# Unions
########################################################################
class ActivityFeed(sgqlc.types.Union):
    __schema__ = zenhub_schema
    __types__ = (Comment, TimelineItem)


class Commentable(sgqlc.types.Union):
    __schema__ = zenhub_schema
    __types__ = (Issue, ZenhubEpic)


class IssueDependencyItem(sgqlc.types.Union):
    __schema__ = zenhub_schema
    __types__ = (Issue, ZenhubEpic)


class Reviewer(sgqlc.types.Union):
    __schema__ = zenhub_schema
    __types__ = (User,)


class RoadmapItem(sgqlc.types.Union):
    __schema__ = zenhub_schema
    __types__ = (Epic, Project, ZenhubEpic)


class WorkspaceSearchMatch(sgqlc.types.Union):
    __schema__ = zenhub_schema
    __types__ = (RepositoryMatch, WorkspaceMatch)


class ZenhubIdentity(sgqlc.types.Union):
    __schema__ = zenhub_schema
    __types__ = (ZenhubOrganization, ZenhubUser)



########################################################################
# Schema Entry Points
########################################################################
zenhub_schema.query_type = Query
zenhub_schema.mutation_type = Mutation
zenhub_schema.subscription_type = None

