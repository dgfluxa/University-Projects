# frozen_string_literal: true

class StudyGroup < ApplicationRecord
  belongs_to :course, optional: false
  belongs_to :study_room, optional: false
  belongs_to :user
  has_many :subscribed_users, dependent: :destroy
end
