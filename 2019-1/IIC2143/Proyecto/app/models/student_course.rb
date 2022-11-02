# frozen_string_literal: true

class StudentCourse < ApplicationRecord
  belongs_to :course, optional: false
  belongs_to :user, optional: false
end
