# frozen_string_literal: true

class Ability
  include CanCan::Ability

  def initialize(user)
    user ||= User.new # guest user (not logged in)
    if user.admin?
      can :manage, :all
    else
      can :manage, Publicacion, user_id: user.id
      can :create, Publicacion
      can :manage, PublicacionComment, user_id: user.id
      can :manage, User, id: user.id
      can :manage, StudyRoomComment, user_id: user.id
      can :create, StudyRoomComment
      can :manage, StudyRoomValoration, user_id: user.id
      can :create, StudyRoomValoration
      can :manage, FavoritePublication, user_id: user.id
      can :manage, StudentCourse, user_id: user.id
      can :manage, ProfessorCourse, user_id: user.id
      can :manage, FavoritePublication, user_id: user.id
      can :manage, StudyGroup, user_id: user.id
      can :create, StudyGroup
      can :manage, Buscoclase
      can :manage, Ofertclase
      can :read, :all
    end

    if user.moderated_courses != []
      user.moderated_courses.each do |moderated|
        can :manage, moderated.course
        can :manage, Publicacion, course_id: moderated.course.id
        can :manage, StudyGroup, course_id: moderated.course.id

        Publicacion.where(course_id: moderated.course.id).each do |publicacion|
          can :manage, publicacion.publicacion_comments
        end
      end
    end

    # Define abilities for the passed in user here. For example:
    #
    #   user ||= User.new # guest user (not logged in)
    #   if user.admin?
    #     can :manage, :all
    #   else
    #     can :read, :all
    #   end
    #
    # The first argument to `can` is the action you are giving the user
    # permission to do.
    # If you pass :manage it will apply to every action. Other common actions
    # here are :read, :create, :update and :destroy.
    #
    # The second argument is the resource the user can perform the action on.
    # If you pass :all it will apply to every resource. Otherwise pass a Ruby
    # class of the resource.
    #
    # The third argument is an optional hash of conditions to further filter the
    # objects.
    # For example, here the user can only update published articles.
    #
    #   can :update, Article, :published => true
    #
    # See the wiki for details:
    # https://github.com/CanCanCommunity/cancancan/wiki/Defining-Abilities
  end
end
