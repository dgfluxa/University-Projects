# frozen_string_literal: true

class StudyRoom < ApplicationRecord
  belongs_to :camp
  has_many :study_groups, dependent: :destroy
  has_many :study_room_comments, dependent: :destroy
  has_many :study_room_valorations, dependent: :destroy
  has_one :occupied_room, dependent: :destroy

  validates :name, presence: true
  validates :ubication, presence: true
end
