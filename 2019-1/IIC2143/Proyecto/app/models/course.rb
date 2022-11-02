# frozen_string_literal: true

class Course < ApplicationRecord
  has_many :student_courses, dependent: :destroy
  has_many :study_groups, dependent: :destroy
  has_many :publicacions, dependent: :destroy
  has_many :moderation_requests, dependent: :destroy
end
